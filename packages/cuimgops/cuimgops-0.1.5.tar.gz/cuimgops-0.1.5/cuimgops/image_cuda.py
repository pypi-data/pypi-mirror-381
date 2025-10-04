import os
import ctypes
import numpy as np
from PIL import Image

# Load horizontal flip library
lib_horizontal_path = os.path.join(os.path.dirname(__file__), "libkernel_horizontal.so")
if not os.path.exists(lib_horizontal_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_horizontal_path}")
lib_h = ctypes.CDLL(lib_horizontal_path)
lib_h.horizontal_flip.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]


def horizontal_flip(image: Image.Image) -> Image.Image:
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = np.zeros_like(arr)

    lib_h.horizontal_flip(
        arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2])
    )
    return Image.fromarray(out_arr)


# Load vertical flip library
lib_vertical_path = os.path.join(os.path.dirname(__file__), "libkernel_vertical.so")
if not os.path.exists(lib_vertical_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_vertical_path}")
lib_v = ctypes.CDLL(lib_vertical_path)
lib_v.vertical_flip.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]

def vertical_flip(image: Image.Image) -> Image.Image:
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = np.zeros_like(arr)

    lib_v.vertical_flip(
        arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2])
    )
    return Image.fromarray(out_arr)



# Load Gaussian noise library
lib_gaussian_path = os.path.join(os.path.dirname(__file__), "libkernel_gaussian_noise.so")
if not os.path.exists(lib_gaussian_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_gaussian_path}")
lib_g = ctypes.CDLL(lib_gaussian_path)
lib_g.add_gaussian_noise.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_float, ctypes.c_float
]

def gaussian_noise(image: Image.Image, mean=0.0, stddev=10.0) -> Image.Image:
    """Add Gaussian noise to a PIL Image using CUDA."""
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = arr.copy()

    lib_g.add_gaussian_noise(
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2]),
        ctypes.c_float(mean),
        ctypes.c_float(stddev)
    )
    return Image.fromarray(out_arr)

# Load Edge Detection library
lib_edge_path = os.path.join(os.path.dirname(__file__), "libkernel_edge_detection.so")
if not os.path.exists(lib_edge_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_edge_path}")
lib_e = ctypes.CDLL(lib_edge_path)
lib_e.edge_detection.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]

def edge_detection(image: Image.Image) -> Image.Image:
    """Apply 3x3 edge detection convolution using CUDA."""
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = np.zeros_like(arr)

    lib_e.edge_detection(
        arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2])
    )
    return Image.fromarray(out_arr)


# Load Blur library
lib_blur_path = os.path.join(os.path.dirname(__file__), "libkernel_blur_conv.so")
if not os.path.exists(lib_blur_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_blur_path}")
lib_b = ctypes.CDLL(lib_blur_path)
lib_b.blur_conv.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]

def blur_conv(image: Image.Image) -> Image.Image:
    """Apply 3x3 blur / smoothing convolution using CUDA."""
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = np.zeros_like(arr)

    lib_b.blur_conv(
        arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2])
    )
    return Image.fromarray(out_arr)

# Load Sharpening library
lib_sharp_path = os.path.join(os.path.dirname(__file__), "libkernel_sharpening_conv.so")
if not os.path.exists(lib_sharp_path):
    raise FileNotFoundError(f"CUDA library not found at {lib_sharp_path}")
lib_s = ctypes.CDLL(lib_sharp_path)
lib_s.sharpening_conv.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]

def sharpening_conv(image: Image.Image) -> Image.Image:
    """Apply 3x3 sharpening convolution using CUDA."""
    img = image.convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    out_arr = np.zeros_like(arr)

    lib_s.sharpening_conv(
        arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        out_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.c_int(arr.shape[1]),
        ctypes.c_int(arr.shape[0]),
        ctypes.c_int(arr.shape[2])
    )
    return Image.fromarray(out_arr)

