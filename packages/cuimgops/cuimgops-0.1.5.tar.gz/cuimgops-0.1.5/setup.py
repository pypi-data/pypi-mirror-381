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

            cmd = ["nvcc", "-shared", "-Xcompiler", "-fPIC", cu_file, "-o", output_file]
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


from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cuimgops",
    version="0.1.5",
    author="Sashank Nimmagadda",
    author_email="sashank.n.1711@gmail.com",
    description="CUDA-accelerated image augmentation operations for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mightycandle/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",
)