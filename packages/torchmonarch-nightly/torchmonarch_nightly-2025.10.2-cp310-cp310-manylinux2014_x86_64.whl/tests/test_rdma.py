# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe
import os

# required to enable RDMA support
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

import pytest
import torch
from monarch.actor import Actor, current_rank, endpoint, this_host
from monarch.rdma import is_rdma_available, RDMABuffer


needs_cuda = pytest.mark.skipif(
    not torch.cuda.is_available(),
    reason="CUDA not available",
)
needs_rdma = pytest.mark.skipif(
    not is_rdma_available(),
    reason="RDMA not available",
)


class ParameterServer(Actor):
    def __init__(self):
        self.params = torch.rand(10, 10)
        self.grad_buffer = torch.rand(10, 10)

    @endpoint
    async def grad_handle(self) -> RDMABuffer:
        byte_tensor = self.grad_buffer.view(torch.uint8).flatten()
        buffer = RDMABuffer(byte_tensor)
        return buffer

    @endpoint
    async def update(self):
        self.params += 0.01 * self.grad_buffer

    @endpoint
    async def get_grad_buffer(self) -> torch.Tensor:
        # just used for testing
        return self.grad_buffer


class ParameterClient(Actor):
    def __init__(self, server, buffer):
        self.server = server
        byte_tensor = buffer.view(torch.uint8).flatten()
        self.buffer = byte_tensor

    @endpoint
    async def upload(self, tensor):
        gh = await self.server.grad_handle.call_one()
        await gh.write_from(tensor)

    @endpoint
    async def download(self):
        gh = await self.server.grad_handle.call_one()
        await gh.read_into(self.buffer)

    @endpoint
    async def get_buffer(self):
        return self.buffer


@needs_rdma
@needs_cuda
async def test_proc_mesh_rdma():
    proc = this_host().spawn_procs(per_host={"gpus": 1})
    server = proc.spawn("server", ParameterServer)

    # --- CPU TESTS ---
    client_cpu = proc.spawn("client_cpu", ParameterClient, server, torch.ones(10, 10))
    x = await client_cpu.get_buffer.call_one()
    assert torch.sum(x.view(torch.float32).view(10, 10)) == 100
    zeros = torch.zeros(10, 10)
    await client_cpu.upload.call_one(zeros.view(torch.uint8).flatten())
    await client_cpu.download.call_one()
    x = await client_cpu.get_buffer.call_one()
    assert torch.sum(x.view(torch.float32).view(10, 10)) == 0

    # --- Modify server's backing buffer directly ---
    await server.update.call_one()

    # Should reflect updated values
    await client_cpu.download.call_one()

    buffer = await client_cpu.get_buffer.call_one()
    remote_grad = await server.get_grad_buffer.call_one()
    assert torch.allclose(buffer.view(torch.float32).view(10, 10), remote_grad)

    # --- GPU TESTS ---
    client_gpu = proc.spawn(
        "client_gpu", ParameterClient, server, torch.ones(10, 10, device="cuda")
    )
    x = await client_gpu.get_buffer.call_one()
    buffer = x.view(torch.float32).view(10, 10)
    assert torch.sum(buffer) == 100
    zeros = torch.zeros(10, 10, device="cuda")
    await client_gpu.upload.call_one(zeros.view(torch.uint8).flatten())
    await client_gpu.download.call_one()
    x = await client_gpu.get_buffer.call_one()
    buffer_gpu = x.view(torch.float32).view(10, 10)
    assert torch.sum(buffer_gpu) == 0

    # Modify server state again
    await server.update.call_one()
    await client_gpu.download.call_one()
    x = await client_gpu.get_buffer.call_one()
    buffer_gpu = x.view(torch.float32).view(10, 10)
    remote_grad = await server.get_grad_buffer.call_one()
    assert torch.allclose(buffer_gpu.cpu(), remote_grad.cpu())


@needs_rdma
async def test_rdma_buffer_drop():
    """Test the new drop() and owner methods on RDMABuffer with two actors"""
    proc = this_host().spawn_procs(per_host={"processes": 1})

    class ProducerActor(Actor):
        def __init__(self):
            self.data = torch.ones(10, 10, dtype=torch.float32)  # 400 bytes
            self.buffer = None

        @endpoint
        async def create_buffer(self) -> RDMABuffer:
            """Create an RDMABuffer and return it"""
            byte_tensor = self.data.view(torch.uint8).flatten()
            self.buffer = RDMABuffer(byte_tensor)
            return self.buffer

    class ConsumerActor(Actor):
        def __init__(self):
            self.received_data = torch.zeros(10, 10, dtype=torch.float32)

        @endpoint
        async def receive_data(self, buffer: RDMABuffer):
            """Receive data from the buffer into local storage"""
            byte_tensor = self.received_data.view(torch.uint8).flatten()
            await buffer.read_into(byte_tensor)  # Read FROM buffer INTO local tensor
            return torch.sum(self.received_data).item()  # Should be 100 (10*10*1)

        @endpoint
        async def test_buffer_after_drop(self, buffer: RDMABuffer):
            """Try to use buffer after it's been dropped - should fail"""
            byte_tensor = self.received_data.view(torch.uint8).flatten()
            try:
                await buffer.read_into(byte_tensor)  # Try to read from dropped buffer
                return "SUCCESS"  # This should not happen
            except Exception as e:
                return f"EXPECTED_ERROR: {e}"

    # Create both actors
    producer = proc.spawn("producer", ProducerActor)
    consumer = proc.spawn("consumer", ConsumerActor)

    # Create an RDMA buffer in the producer
    buffer = await producer.create_buffer.call_one()

    # Pass buffer to consumer and test write operation
    result = await consumer.receive_data.call_one(buffer)
    assert result == 100.0, f"Expected 100.0, got {result}"

    # Now drop the buffer
    await buffer.drop()

    # Test that we can call drop multiple times (should be idempotent)
    await buffer.drop()

    # Try to use the buffer after dropping - this should fail
    error_result = await consumer.test_buffer_after_drop.call_one(buffer)
    assert error_result.startswith(
        "EXPECTED_ERROR:"
    ), f"Expected an error after drop, but got: {error_result}"

    print(f"✓ Buffer operations failed after drop as expected: {error_result}")


class TrainerActor(Actor):
    def __init__(self):
        super().__init__()
        self.trainer = torch.nn.Linear(10, 10).to("cuda")
        self.trainer.weight.data.zero_()

    @endpoint
    async def init(self, gen):
        ranks = current_rank()
        self.gen = gen.slice(**ranks)

    @endpoint
    async def exchange_metadata(self):
        byte_tensor = self.trainer.weight.data.view(torch.uint8).flatten()
        self.handle = RDMABuffer(byte_tensor)
        await self.gen.attach_weight_buffer.call(self.handle)

    @endpoint
    async def weights_ready(self):
        self.trainer.weight.data.add_(1.0)


class GeneratorActor(Actor):
    def __init__(self):
        super().__init__()
        self.generator = torch.nn.Linear(10, 10).to("cuda")
        self.step = 0

    @endpoint
    async def init(self, trainer):
        ranks = current_rank()
        self.trainer = trainer.slice(**ranks)

    @endpoint
    async def attach_weight_buffer(self, handle):
        self.handle = handle

    @endpoint
    async def update_weights(self):
        self.step += 1
        byte_tensor = self.generator.weight.data.view(torch.uint8).flatten()
        await self.handle.read_into(byte_tensor)
        assert (
            torch.sum(self.generator.weight.data) == self.step * 100
        ), f"{torch.sum(self.generator.weight.data)=}, {self.step=}"


@needs_rdma
@needs_cuda
async def test_gpu_trainer_generator():
    trainer_proc = this_host().spawn_procs(per_host={"gpus": 2})
    gen_proc = this_host().spawn_procs(per_host={"gpus": 2})
    trainer = trainer_proc.spawn("trainer", TrainerActor)
    generator = gen_proc.spawn("gen", GeneratorActor)

    await generator.init.call(trainer)
    await trainer.init.call(generator)
    await trainer.exchange_metadata.call()

    for _ in range(3):
        await trainer.weights_ready.call()
        await generator.update_weights.call()


@needs_rdma
@needs_cuda
def test_gpu_trainer_generator_sync() -> None:
    trainer_proc = this_host().spawn_procs(per_host={"gpus": 1})
    gen_proc = this_host().spawn_procs(per_host={"gpus": 1})
    trainer = trainer_proc.spawn("trainer", TrainerActor)
    generator = gen_proc.spawn("gen", GeneratorActor)

    generator.init.call(trainer).get()
    trainer.init.call(generator).get()
    trainer.exchange_metadata.call().get()

    for _ in range(1):
        trainer.weights_ready.call().get()
        generator.update_weights.call().get()


@needs_rdma
async def test_rdma_concurrent_2gb_writes_in_order():
    """Test concurrent 2GB RDMA buffer writes with reverse-order awaiting"""
    proc = this_host().spawn_procs(per_host={"processes": 1})
    num_elem = 500_000_000  # 500M elements

    class BufferOwnerActor(Actor):
        def __init__(self):
            # Create a 2GB buffer (500M float32 elements * 4 bytes = 2GB)
            self.data = torch.zeros(num_elem, dtype=torch.float32)
            self.rdma_buffer = None

        @endpoint
        async def create_buffer(self) -> RDMABuffer:
            """Create a 2GB RDMABuffer"""
            byte_tensor = self.data.view(torch.uint8).flatten()
            self.rdma_buffer = RDMABuffer(byte_tensor)
            return self.rdma_buffer

        @endpoint
        async def get_buffer_data(self) -> torch.Tensor:
            """Return the current buffer data for verification"""
            return self.data

    class WriterActor(Actor):
        def __init__(self):
            # Create a 2GB buffer (500M float32 elements * 4 bytes = 2GB)
            self.tensor_a = torch.ones(
                num_elem, dtype=torch.float32
            )  # Will receive data
            self.tensor_b = torch.full(
                (num_elem,), 2.0, dtype=torch.float32
            )  # Will send data

        @endpoint
        async def perform_concurrent_writes(self, buffer: RDMABuffer):
            """Perform concurrent read/write operations and await in reverse order"""
            # Convert tensors to byte views for RDMA
            byte_tensor_a = self.tensor_a.view(torch.uint8).flatten()
            byte_tensor_b = self.tensor_b.view(torch.uint8).flatten()

            # Start both operations concurrently
            future_a = buffer.read_into(
                byte_tensor_a, timeout=10
            )  # Read FROM buffer INTO tensor_a
            future_b = buffer.write_from(
                byte_tensor_b, timeout=10
            )  # Write FROM tensor_b INTO buffer

            # Await in reverse order - sets actual execution order
            await future_b  # Await write operation first
            await future_a  # Await read operation second

            return "SUCCESS"

        @endpoint
        async def get_tensors(self) -> tuple[torch.Tensor, torch.Tensor]:
            """Return both tensors for verification"""
            return (self.tensor_a, self.tensor_b)

    # Create actors
    buffer_owner = proc.spawn("buffer_owner", BufferOwnerActor)
    writer = proc.spawn("writer", WriterActor)

    # Create the 2GB RDMA buffer
    buffer = await buffer_owner.create_buffer.call_one()
    print(f"✓ Created 2GB RDMA buffer (size: {buffer.size() / (1024**3):.2f} GB)")

    # Perform concurrent writes with reverse-order awaiting
    result = await writer.perform_concurrent_writes.call_one(buffer)
    assert result == "SUCCESS", f"Concurrent writes failed: {result}"

    # Verify the data flow worked correctly using torch.allclose
    tensor_a_actual, tensor_b_actual = await writer.get_tensors.call_one()
    buffer_data_actual = await buffer_owner.get_buffer_data.call_one()

    expected_result = torch.full((num_elem,), 2.0, dtype=torch.float32)

    # Verify using torch.allclose
    assert torch.allclose(
        tensor_a_actual, expected_result
    ), "tensor_a does not match expected 2.0s"
    assert torch.allclose(
        tensor_b_actual, expected_result
    ), "tensor_b does not match expected 2.0s"

    assert torch.allclose(
        buffer_data_actual, expected_result
    ), "RDMABuffer does not contain expected 2.0s"

    print("✓ Concurrent 2GB operations completed successfully")

    # Drop the buffer
    await buffer.drop()
    print("✓ Buffer dropped successfully")
