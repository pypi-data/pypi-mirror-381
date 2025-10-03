# cuimgops

CUDA-accelerated image augmentation operations for Python.

## Features
- **Augmentation**
  - Horizontal Flip
  - Vertical Flip

- **Convolution**
  - Gaussian Noise
  - Edge Detection
  - Blur (Smoothing)
  - Sharpening
  
- **In Development**
    - Multiple images - Batched convolution on streams

## Installation

```bash
pip install cuimgops
```

## Usage

```python
from cuimgops import *
from PIL import Image

img = Image.open("image.jpg")

flipped = get_horizontal_flip(img)
noisy = get_gaussian_noise(img, mean=0.0, stddev=15.0)
edges = get_edge_detection(img)
blurred = get_blur(img)
sharpened = get_sharpening(img)
```
