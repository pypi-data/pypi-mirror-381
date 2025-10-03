"""Smoke tests for omnigpu.auto_patch on the current machine."""

import torch
import omnigpu.auto_patch as auto_patch


def test_tensor_creation():
    auto_patch.patch()
    try:
        tensor = torch.randn(4, 4, device='cuda')
        assert tensor.is_cuda or tensor.device.type in {'mps', 'cpu'}
    finally:
        auto_patch.unpatch()


def test_module_to_device():
    auto_patch.patch()
    try:
        model = torch.nn.Linear(4, 2).cuda()
        assert any(param.device.type in {'cuda', 'mps', 'cpu'} for param in model.parameters())
    finally:
        auto_patch.unpatch()
