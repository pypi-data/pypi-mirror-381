# cuimgops

CUDA-accelerated image augmentation operations for Python.

## Features

- Horizontal flip
- Vertical flip
- Gaussian noise
- Edge detection
- Blur (smoothing)
- Sharpening

## Installation

```bash
pip install cuimgops
```

## Requirements

- CUDA-capable GPU
- CUDA Toolkit
- Python >= 3.8
- numpy
- pillow

## Usage

```python
from cuimgops import (
    get_horizontal_flip,
    get_vertical_flip,
    get_gaussian_noise,
    get_edge_detection,
    get_blur,
    get_sharpening
)
from PIL import Image

img = Image.open("image.jpg")

flipped = get_horizontal_flip(img)
noisy = get_gaussian_noise(img, mean=0.0, stddev=15.0)
edges = get_edge_detection(img)
blurred = get_blur(img)
sharpened = get_sharpening(img)
```

## Author

sashank nimmagadda

## License

MIT