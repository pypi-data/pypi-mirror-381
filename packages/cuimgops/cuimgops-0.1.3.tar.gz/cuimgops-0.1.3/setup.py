from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import os
import shutil

class CudaExtension(Extension):
    def __init__(self, name, sources):
        super().__init__(name, sources=sources)

class BuildCudaExt(build_ext):
    def build_extension(self, ext):
        if isinstance(ext, CudaExtension):
            output_file = self.get_ext_fullpath(ext.name)
            cu_file = ext.sources[0]
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            cmd = ["nvcc", "-arch=sm_75", "-shared", "-Xcompiler", "-fPIC", cu_file, "-o", output_file]
            subprocess.check_call(cmd)

            if "kernel_horizontal.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_horizontal.so")
            elif "kernel_vertical.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_vertical.so")
            elif "kernel_gaussian_noise.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_gaussian_noise.so")
            elif "kernel_edge_detection.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_edge_detection.so")
            elif "kernel_blur_conv.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_blur_conv.so")
            elif "kernel_sharpening_conv.cu" in cu_file:
                package_lib_path = os.path.join(os.path.dirname(__file__), "cuimgops", "libkernel_sharpening_conv.so")
                
            shutil.copy2(output_file, package_lib_path)    
            super().build_extension(ext)
ext_modules_src=[
    CudaExtension("cuimgops.kernel_horizontal", ["cuimgops/kernel_horizontal.cu"]),
    CudaExtension("cuimgops.kernel_vertical", ["cuimgops/kernel_vertical.cu"]),
    CudaExtension("cuimgops.kernel_gaussian_noise", ["cuimgops/kernel_gaussian_noise.cu"]),
    CudaExtension("cuimgops.kernel_edge_detection", ["cuimgops/kernel_edge_detection.cu"]),
    CudaExtension("cuimgops.kernel_blur_conv", ["cuimgops/kernel_blur_conv.cu"]),
    CudaExtension("cuimgops.kernel_sharpening_conv", ["cuimgops/kernel_sharpening_conv.cu"])
]

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "CUDA accelerated image augmentations"

setup(
    name="cuimgops",
    version="0.1.3",
    description="CUDA accelerated image processing operations with Python bindings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sashank Nimmagadda",
    url="https://github.com/mightycandle",
    packages=["cuimgops"],
    package_data={"cuimgops": ["*.so", "*.cu"]},
    include_package_data=True,
    cmdclass={"build_ext": BuildCudaExt},
    ext_modules=ext_modules_src,
    python_requires=">=3.8",
    install_requires=[
        "numpy",
    ],
    extras_require={
        "dev": ["matplotlib", "pillow"],
    },
    keywords="cuda image-processing gpu numpy python c++",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: C",
        "Programming Language :: C++",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "License :: OSI Approved :: MIT License",
    ]
)