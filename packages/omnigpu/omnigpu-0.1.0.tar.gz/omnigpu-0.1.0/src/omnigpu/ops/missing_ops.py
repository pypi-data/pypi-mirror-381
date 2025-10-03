"""Implementation of missing critical operations for OmniGPU."""

import torch
from typing import Optional, Tuple, Union

def patch_missing_operations():
    """Patch PyTorch with MPS implementations of missing operations."""
    
    # 1. Gather operation (critical for transformers)
    original_gather = torch.gather
    def mps_gather(input, dim, index):
        if input.device.type == 'mps':
            # Move to CPU, perform operation, move back
            cpu_result = original_gather(input.cpu(), dim, index.cpu())
            return cpu_result.to('mps')
        return original_gather(input, dim, index)
    torch.gather = mps_gather
    
    # 2. Scatter operation (critical for sparse operations)
    original_scatter = torch.scatter
    def mps_scatter(input, dim, index, src):
        if input.device.type == 'mps':
            cpu_result = original_scatter(input.cpu(), dim, index.cpu(), src.cpu())
            return cpu_result.to('mps')
        return original_scatter(input, dim, index, src)
    torch.scatter = mps_scatter
    
    # 3. Embedding (critical for NLP)
    original_embedding = torch.nn.functional.embedding
    def mps_embedding(input, weight, padding_idx=None, max_norm=None, 
                     norm_type=2., scale_grad_by_freq=False, sparse=False):
        if weight.device.type == 'mps':
            # Use native MPS embedding if available, otherwise CPU fallback
            try:
                return original_embedding(input, weight, padding_idx, max_norm, 
                                        norm_type, scale_grad_by_freq, sparse)
            except:
                cpu_input = input.cpu() if input.is_cuda or input.device.type == 'mps' else input
                cpu_weight = weight.cpu()
                result = original_embedding(cpu_input, cpu_weight, padding_idx, 
                                          max_norm, norm_type, scale_grad_by_freq, sparse)
                return result.to(weight.device)
        return original_embedding(input, weight, padding_idx, max_norm, 
                                norm_type, scale_grad_by_freq, sparse)
    torch.nn.functional.embedding = mps_embedding
    
    # 4. Arange (tensor creation)
    original_arange = torch.arange
    def mps_arange(*args, **kwargs):
        device = kwargs.get('device', None)
        if device and 'mps' in str(device):
            # Create on CPU first, then move to MPS
            kwargs['device'] = 'cpu'
            result = original_arange(*args, **kwargs)
            return result.to('mps')
        return original_arange(*args, **kwargs)
    torch.arange = mps_arange
    
    # 5. Eye (identity matrix)
    original_eye = torch.eye
    def mps_eye(*args, **kwargs):
        device = kwargs.get('device', None)
        if device and 'mps' in str(device):
            kwargs['device'] = 'cpu'
            result = original_eye(*args, **kwargs)
            return result.to('mps')
        return original_eye(*args, **kwargs)
    torch.eye = mps_eye
    
    # 6. Linear algebra operations
    # BMM (Batch Matrix Multiply)
    original_bmm = torch.bmm
    def mps_bmm(input, mat2):
        if input.device.type == 'mps':
            try:
                return original_bmm(input, mat2)
            except:
                # Fallback to CPU
                return original_bmm(input.cpu(), mat2.cpu()).to('mps')
        return original_bmm(input, mat2)
    torch.bmm = mps_bmm
    
    print("✅ Patched 6 critical missing operations with MPS support")