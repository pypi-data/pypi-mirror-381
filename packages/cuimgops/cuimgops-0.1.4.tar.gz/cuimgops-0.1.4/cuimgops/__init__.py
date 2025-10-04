from .image_cuda import (
    horizontal_flip as _h_flip,
    vertical_flip as _v_flip,
    gaussian_noise as _gaussian,
    edge_detection as _edge,
    blur_conv as _blur,
    sharpening_conv as _sharpen
)
from PIL import Image

# exposed functions
def get_horizontal_flip(image: Image.Image) -> Image.Image:
    """Return horizontal flipped image."""
    return _h_flip(image)

def get_vertical_flip(image: Image.Image) -> Image.Image:
    """Return vertical flipped image."""
    return _v_flip(image)

def get_gaussian_noise(image: Image.Image, mean=0.0, stddev=15.0) -> Image.Image:
    """Return image with Gaussian noise applied."""
    return _gaussian(image, mean, stddev)

def get_edge_detection(image: Image.Image) -> Image.Image:
    """Return edge-detected image."""
    return _edge(image)

def get_blur(image: Image.Image) -> Image.Image:
    """Return blurred/smoothened image."""
    return _blur(image)

def get_sharpening(image: Image.Image) -> Image.Image:
    """Return sharpened image."""
    return _sharpen(image)

# Export for import *
__all__ = [
    "get_horizontal_flip",
    "get_vertical_flip",
    "get_gaussian_noise",
    "get_edge_detection",
    "get_blur",
    "get_sharpening"
]
