# Simple EXR

A simple Python library for reading and writing OpenEXR files using numpy arrays.

## Installation

```bash
pip install simple-exr
```

## Quick Start

### Reading EXR Files

```python
import simple_exr
import numpy as np

# Read an EXR file
image = simple_exr.read_exr("path/to/image.exr")
print(f"Image shape: {image.shape}")  # (height, width, channels)
print(f"Image dtype: {image.dtype}")  # float32
```

### Writing EXR Files

```python
import simple_exr
import numpy as np

# Create a sample RGB image
height, width = 512, 512
rgb_image = np.random.rand(height, width, 3).astype(np.float32)

# Write to EXR file
simple_exr.write_exr("output.exr", rgb_image)

# Create a sample RGBA image
rgba_image = np.random.rand(height, width, 4).astype(np.float32)

# Write RGBA to EXR file
simple_exr.write_exr("output_rgba.exr", rgba_image)
```

## API Reference

### `read_exr(path: str) -> np.ndarray`

Read an EXR file and return it as a numpy array.

**Parameters:**
- `path` (str): Path to the EXR file

**Returns:**
- `np.ndarray`: Image data as (H, W, C) array where C is 3 (RGB) or 4 (RGBA)

**Raises:**
- `ValueError`: If no RGB(A) channels are found in the EXR file
- `FileNotFoundError`: If the file doesn't exist

### `write_exr(path: str, img: np.ndarray)`

Write a numpy array to an EXR file as RGB or RGBA depending on channel count.

**Parameters:**
- `path` (str): Output path for the EXR file
- `img` (np.ndarray): Image data with shape (H, W, 3) or (H, W, 4), dtype float32 or float64

**Raises:**
- `ValueError`: If img doesn't have 3 or 4 channels
