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

setup(
    name="cuimgops",
    version="0.1.4",
    packages=["cuimgops"],
    
    ext_modules=[
        CudaExtension("cuimgops.kernel_horizontal", ["cuimgops/kernel_horizontal.cu"]),
        CudaExtension("cuimgops.kernel_vertical", ["cuimgops/kernel_vertical.cu"]),
        CudaExtension("cuimgops.kernel_gaussian_noise", ["cuimgops/kernel_gaussian_noise.cu"]),
        CudaExtension("cuimgops.kernel_edge_detection", ["cuimgops/kernel_edge_detection.cu"]),
        CudaExtension("cuimgops.blur_conv", ["cuimgops/kernel_blur_conv.cu"]),
        CudaExtension("cuimgops.kernel_sharpening_conv", ["cuimgops/kernel_sharpening_conv.cu"])
    ],
    cmdclass={'build_ext': BuildCudaExt},
)