#include <cuda_runtime.h>
#include <stdint.h>
#include <iostream>
#include <chrono>
extern "C" {

// 3x3 sharpening kernel
__constant__ int kernel[3][3] = {
    {  0, -1,  0 },
    { -1,  5, -1 },
    {  0, -1,  0 }
};

__global__ void sharpening_kernel(const uint8_t* input, uint8_t* output, int width, int height, int channels) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < 1 || x >= width-1 || y < 1 || y >= height-1) return; // skip borders

    for (int c = 0; c < channels; ++c) {
        int sum = 0;
        for (int ky = -1; ky <= 1; ++ky) {
            for (int kx = -1; kx <= 1; ++kx) {
                int px = x + kx;
                int py = y + ky;
                sum += input[(py*width + px)*channels + c] * kernel[ky+1][kx+1];
            }
        }
        if (sum < 0) sum = 0;
        if (sum > 255) sum = 255;
        output[(y*width + x)*channels + c] = (uint8_t)sum;
    }
}

void sharpening_conv(uint8_t* input, uint8_t* output, int width, int height, int channels) {
    uint8_t *d_input, *d_output;
    size_t size = width * height * channels * sizeof(uint8_t);
    cudaMalloc(&d_input, size);
    cudaMalloc(&d_output, size);
    
    cudaMemcpy(d_input, input, size, cudaMemcpyHostToDevice);
    
    dim3 block(16,16);
    dim3 grid((width + block.x - 1)/block.x, (height + block.y - 1)/block.y);
    
    auto start = std::chrono::high_resolution_clock::now();

    sharpening_kernel<<<grid, block>>>(d_input, d_output, width, height, channels);
    
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> elapsed = end - start;
    // std::cout << "[GPU] sharpening_conv time: " << elapsed.count() << " ms" << std::endl;
    
    
    cudaMemcpy(output, d_output, size, cudaMemcpyDeviceToHost);
    cudaFree(d_input);
    cudaFree(d_output);
}
}