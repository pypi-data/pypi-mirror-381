"""Advanced indexing operations for transformer and NLP model support.

This module implements critical indexing operations that are essential for
modern transformer architectures, attention mechanisms, and advanced NLP models.
"""

import torch
import logging
from typing import Optional, Union, Tuple, List

logger = logging.getLogger("omnigpu.advanced_indexing")


def patch_advanced_indexing_operations():
    """Patch PyTorch with enhanced indexing operations for MPS compatibility."""
    
    logger.info("Applying advanced indexing operation patches...")
    patches_applied = 0
    
    # ========== INDEX_PUT OPERATION ==========
    # Critical for scatter operations in attention mechanisms
    original_index_put = torch.index_put
    
    def omnigpu_index_put(input, indices, values, accumulate=False):
        """Enhanced index_put with MPS/CPU fallback."""
        try:
            # Try native MPS first for simple cases
            if input.device.type == 'mps' and len(indices) == 1:
                return original_index_put(input, indices, values, accumulate)
        except Exception:
            pass
        
        # CPU fallback for complex indexing
        device = input.device
        input_cpu = input.cpu()
        values_cpu = values.cpu() if hasattr(values, 'cpu') else values
        indices_cpu = tuple(idx.cpu() if hasattr(idx, 'cpu') else idx for idx in indices)
        
        result = original_index_put(input_cpu, indices_cpu, values_cpu, accumulate)
        return result.to(device)
    
    torch.index_put = omnigpu_index_put
    torch.Tensor.index_put = lambda self, indices, values, accumulate=False: omnigpu_index_put(self, indices, values, accumulate)
    torch.Tensor.index_put_ = lambda self, indices, values, accumulate=False: self.copy_(omnigpu_index_put(self, indices, values, accumulate))
    patches_applied += 1
    
    # ========== INDEX_ADD OPERATION ==========
    # Essential for accumulation patterns in transformers
    original_index_add = torch.index_add
    
    def omnigpu_index_add(input, dim, index, source, *, alpha=1):
        """Enhanced index_add with MPS/CPU fallback."""
        try:
            # Try native MPS first
            if input.device.type == 'mps' and alpha == 1:
                return original_index_add(input, dim, index, source)
        except Exception:
            pass
        
        # CPU fallback
        device = input.device
        input_cpu = input.cpu()
        index_cpu = index.cpu()
        source_cpu = source.cpu()
        
        result = original_index_add(input_cpu, dim, index_cpu, source_cpu, alpha=alpha)
        return result.to(device)
    
    torch.index_add = omnigpu_index_add
    torch.Tensor.index_add = lambda self, dim, index, source, *, alpha=1: omnigpu_index_add(self, dim, index, source, alpha=alpha)
    torch.Tensor.index_add_ = lambda self, dim, index, source, *, alpha=1: self.copy_(omnigpu_index_add(self, dim, index, source, alpha=alpha))
    patches_applied += 1
    
    # ========== TAKE_ALONG_DIM OPERATION ==========
    # Critical for dynamic indexing in attention and advanced transformers
    if hasattr(torch, 'take_along_dim'):
        original_take_along_dim = torch.take_along_dim
    else:
        # Implement if not available in older PyTorch versions
        def original_take_along_dim(input, indices, dim=None):
            if dim is None:
                return torch.take(input.flatten(), indices.flatten()).reshape(indices.shape)
            return torch.gather(input, dim, indices)
    
    def omnigpu_take_along_dim(input, indices, dim=None):
        """Enhanced take_along_dim with MPS/CPU fallback."""
        try:
            # Try native MPS first
            if input.device.type == 'mps':
                if dim is None:
                    # Flatten and take approach for MPS
                    flat_input = input.flatten()
                    flat_indices = indices.flatten()
                    result = torch.gather(flat_input.unsqueeze(0), 0, flat_indices.unsqueeze(0))
                    return result.squeeze(0).reshape(indices.shape)
                else:
                    return torch.gather(input, dim, indices)
        except Exception:
            pass
        
        # CPU fallback
        device = input.device
        input_cpu = input.cpu()
        indices_cpu = indices.cpu()
        
        result = original_take_along_dim(input_cpu, indices_cpu, dim)
        return result.to(device)
    
    torch.take_along_dim = omnigpu_take_along_dim
    patches_applied += 1
    
    # ========== REPEAT_INTERLEAVE OPERATION ==========
    # Essential for positional encoding and sequence operations
    original_repeat_interleave = torch.repeat_interleave
    
    def omnigpu_repeat_interleave(input, repeats, dim=None, *, output_size=None):
        """Enhanced repeat_interleave with MPS/CPU fallback."""
        try:
            # Try native MPS first for simple cases
            if input.device.type == 'mps' and output_size is None:
                if isinstance(repeats, int):
                    return original_repeat_interleave(input, repeats, dim)
        except Exception:
            pass
        
        # CPU fallback for complex cases
        device = input.device
        input_cpu = input.cpu()
        repeats_cpu = repeats.cpu() if hasattr(repeats, 'cpu') else repeats
        
        result = original_repeat_interleave(input_cpu, repeats_cpu, dim, output_size=output_size)
        return result.to(device)
    
    torch.repeat_interleave = omnigpu_repeat_interleave
    torch.Tensor.repeat_interleave = lambda self, repeats, dim=None, output_size=None: omnigpu_repeat_interleave(self, repeats, dim, output_size=output_size)
    patches_applied += 1
    
    # ========== ENHANCED SCATTER OPERATIONS ==========
    # Improve existing scatter operations for better transformer support
    original_scatter = torch.scatter
    
    def omnigpu_scatter(input, dim, index, src, *, reduce=None):
        """Enhanced scatter with better MPS support."""
        try:
            # Try native MPS first
            if input.device.type == 'mps' and reduce is None:
                return original_scatter(input, dim, index, src)
        except Exception:
            pass
        
        # CPU fallback for complex cases
        device = input.device
        input_cpu = input.cpu()
        index_cpu = index.cpu()
        src_cpu = src.cpu() if hasattr(src, 'cpu') else src
        
        if reduce is not None:
            result = original_scatter(input_cpu, dim, index_cpu, src_cpu, reduce=reduce)
        else:
            result = original_scatter(input_cpu, dim, index_cpu, src_cpu)
        return result.to(device)
    
    torch.scatter = omnigpu_scatter
    torch.Tensor.scatter = lambda self, dim, index, src, reduce=None: omnigpu_scatter(self, dim, index, src, reduce=reduce)
    torch.Tensor.scatter_ = lambda self, dim, index, src, reduce=None: self.copy_(omnigpu_scatter(self, dim, index, src, reduce=reduce))
    patches_applied += 1
    
    # ========== SEARCHSORTED OPERATION ==========
    # Useful for bucketing and advanced indexing patterns
    if hasattr(torch, 'searchsorted'):
        original_searchsorted = torch.searchsorted
        
        def omnigpu_searchsorted(sorted_sequence, values, *, out_int32=False, right=False, side=None, sorter=None):
            """Enhanced searchsorted with MPS/CPU fallback."""
            # Always use CPU fallback for now - complex operation
            device = sorted_sequence.device
            seq_cpu = sorted_sequence.cpu()
            values_cpu = values.cpu()
            sorter_cpu = sorter.cpu() if sorter is not None else None
            
            # Handle different PyTorch versions
            if side is not None:
                result = original_searchsorted(seq_cpu, values_cpu, out_int32=out_int32, side=side, sorter=sorter_cpu)
            else:
                result = original_searchsorted(seq_cpu, values_cpu, out_int32=out_int32, right=right, sorter=sorter_cpu)
            
            return result.to(device)
        
        torch.searchsorted = omnigpu_searchsorted
        torch.Tensor.searchsorted = lambda self, values, out_int32=False, right=False, side=None, sorter=None: omnigpu_searchsorted(self, values, out_int32=out_int32, right=right, side=side, sorter=sorter)
        patches_applied += 1
    
    # ========== BUCKETIZE OPERATION ==========
    # Useful for discretization in transformers
    if hasattr(torch, 'bucketize'):
        original_bucketize = torch.bucketize
        
        def omnigpu_bucketize(input, boundaries, *, out_int32=False, right=False):
            """Enhanced bucketize with MPS/CPU fallback."""
            # CPU fallback - complex operation
            device = input.device
            input_cpu = input.cpu()
            boundaries_cpu = boundaries.cpu()
            
            result = original_bucketize(input_cpu, boundaries_cpu, out_int32=out_int32, right=right)
            return result.to(device)
        
        torch.bucketize = omnigpu_bucketize
        torch.Tensor.bucketize = lambda self, boundaries, out_int32=False, right=False: omnigpu_bucketize(self, boundaries, out_int32=out_int32, right=right)
        patches_applied += 1
    
    logger.info(f"✅ Applied {patches_applied} advanced indexing patches")
    return patches_applied


def test_advanced_indexing():
    """Test the advanced indexing operations."""
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Testing advanced indexing operations on {device}...")
    
    tests_passed = 0
    total_tests = 0
    
    # Test index_put
    try:
        total_tests += 1
        input_tensor = torch.zeros(3, 3, device=device)
        indices = (torch.tensor([0, 1], device=device), torch.tensor([1, 2], device=device))
        values = torch.tensor([1.0, 2.0], device=device)
        result = torch.index_put(input_tensor, indices, values)
        assert result[0, 1] == 1.0 and result[1, 2] == 2.0
        tests_passed += 1
        print("✅ index_put test passed")
    except Exception as e:
        print(f"❌ index_put test failed: {e}")
    
    # Test index_add
    try:
        total_tests += 1
        input_tensor = torch.zeros(3, 3, device=device)
        dim = 0
        index = torch.tensor([0, 1, 0], device=device)
        source = torch.ones(3, 3, device=device)
        result = torch.index_add(input_tensor, dim, index, source)
        assert result[0, 0] == 2.0  # Added twice to index 0
        tests_passed += 1
        print("✅ index_add test passed")
    except Exception as e:
        print(f"❌ index_add test failed: {e}")
    
    # Test take_along_dim
    try:
        total_tests += 1
        input_tensor = torch.arange(12, device=device).reshape(3, 4)
        indices = torch.tensor([[0, 2], [1, 3]], device=device)
        result = torch.take_along_dim(input_tensor, indices, dim=1)
        assert result.shape == (2, 2)
        tests_passed += 1
        print("✅ take_along_dim test passed")
    except Exception as e:
        print(f"❌ take_along_dim test failed: {e}")
    
    # Test repeat_interleave
    try:
        total_tests += 1
        input_tensor = torch.tensor([1, 2, 3], device=device)
        result = torch.repeat_interleave(input_tensor, 2)
        expected = torch.tensor([1, 1, 2, 2, 3, 3], device=device)
        assert torch.equal(result, expected)
        tests_passed += 1
        print("✅ repeat_interleave test passed")
    except Exception as e:
        print(f"❌ repeat_interleave test failed: {e}")
    
    print(f"\nAdvanced indexing tests: {tests_passed}/{total_tests} passed")
    return tests_passed == total_tests


if __name__ == "__main__":
    # Apply patches and test
    patch_advanced_indexing_operations()
    test_advanced_indexing()