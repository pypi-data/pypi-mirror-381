"""
Simple test script for GPU integration (no pytest required).
"""

import numpy as np
import sys


def test_gpu_wrapper_function_exists():
    """Test that GPU wrapper function can be imported."""
    print("Testing GPU wrapper function import...")
    from ign_lidar.features import compute_all_features_with_gpu
    assert compute_all_features_with_gpu is not None
    print("✓ GPU wrapper function exists")


def test_gpu_module_availability():
    """Test GPU module import and availability detection."""
    print("\nTesting GPU module availability...")
    try:
        from ign_lidar.features_gpu import (
            GPUFeatureComputer,
            GPU_AVAILABLE,
            CUML_AVAILABLE
        )
        
        # Module imports successfully
        assert GPUFeatureComputer is not None
        assert isinstance(GPU_AVAILABLE, bool)
        assert isinstance(CUML_AVAILABLE, bool)
        
        if GPU_AVAILABLE:
            print("✓ GPU (CuPy) is available")
        else:
            print("⚠ GPU (CuPy) not available - CPU fallback will be used")
            
        if CUML_AVAILABLE:
            print("✓ RAPIDS cuML is available")
        else:
            print("⚠ RAPIDS cuML not available")
            
    except ImportError as e:
        print(f"✓ GPU module import handled gracefully: {e}")


def test_gpu_wrapper_cpu_fallback():
    """Test GPU wrapper works with CPU fallback."""
    print("\nTesting CPU fallback...")
    from ign_lidar.features import compute_all_features_with_gpu
    
    # Create sample data
    np.random.seed(42)
    points = np.random.rand(1000, 3).astype(np.float32)
    points[:, 2] *= 10  # Scale Z for more realistic heights
    classification = np.random.randint(1, 6, size=1000, dtype=np.uint8)
    
    # Test with GPU disabled (should always work)
    normals, curvature, height, geo_features = compute_all_features_with_gpu(
        points, classification, k=10, auto_k=False, use_gpu=False
    )
    
    # Verify shapes
    assert normals.shape == (1000, 3), \
        f"Expected (1000, 3), got {normals.shape}"
    assert curvature.shape == (1000,), \
        f"Expected (1000,), got {curvature.shape}"
    assert height.shape == (1000,), \
        f"Expected (1000,), got {height.shape}"
    
    # Verify normals are normalized
    norms = np.linalg.norm(normals, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-5), "Normals should be normalized"
    
    # Verify geometric features
    expected_features = [
        'planarity', 'linearity', 'sphericity',
        'anisotropy', 'roughness', 'density'
    ]
    for feat in expected_features:
        assert feat in geo_features, f"Missing feature: {feat}"
        assert geo_features[feat].shape == (1000,), \
            f"Feature {feat} has wrong shape: {geo_features[feat].shape}"
    
    print("✓ CPU fallback works correctly")
    print(f"  - Computed normals: {normals.shape}")
    print(f"  - Computed curvature: {curvature.shape}")
    print(f"  - Computed height: {height.shape}")
    print(f"  - Computed {len(geo_features)} geometric features")


def test_gpu_wrapper_with_gpu_enabled():
    """Test GPU wrapper with GPU enabled (falls back if not available)."""
    print("\nTesting with GPU enabled...")
    from ign_lidar.features import compute_all_features_with_gpu
    
    # Create sample data
    np.random.seed(42)
    points = np.random.rand(1000, 3).astype(np.float32)
    points[:, 2] *= 10
    classification = np.random.randint(1, 6, size=1000, dtype=np.uint8)
    
    # Test with GPU enabled (will fallback to CPU if GPU not available)
    normals, curvature, height, geo_features = compute_all_features_with_gpu(
        points, classification, k=10, auto_k=False, use_gpu=True
    )
    
    # Verify shapes (should work regardless of GPU availability)
    assert normals.shape == (1000, 3)
    assert curvature.shape == (1000,)
    assert height.shape == (1000,)
    assert len(geo_features) >= 6  # At least 6 geometric features
    
    print("✓ GPU wrapper with GPU enabled works")
    print("  (Used GPU if available, otherwise fell back to CPU)")


def main():
    """Run all tests."""
    print("=" * 60)
    print("GPU Integration Tests")
    print("=" * 60)
    
    try:
        test_gpu_wrapper_function_exists()
        test_gpu_module_availability()
        test_gpu_wrapper_cpu_fallback()
        test_gpu_wrapper_with_gpu_enabled()
        
        print("\n" + "=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        return 0
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
