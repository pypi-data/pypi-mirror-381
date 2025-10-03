#include <cuda_runtime.h>
#include <stdint.h>

extern "C" {

// Simple 3x3 averaging kernel
__constant__ float kernel[3][3] = {
    { 1.0f/9, 1.0f/9, 1.0f/9 },
    { 1.0f/9, 1.0f/9, 1.0f/9 },
    { 1.0f/9, 1.0f/9, 1.0f/9 }
};

__global__ void blur_kernel(const uint8_t* input, uint8_t* output, int width, int height, int channels) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < 1 || x >= width-1 || y < 1 || y >= height-1) return; // skip borders

    for (int c = 0; c < channels; ++c) {
        float sum = 0.0f;
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

void blur_conv(uint8_t* input, uint8_t* output, int width, int height, int channels) {
    uint8_t *d_input, *d_output;
    size_t size = width * height * channels * sizeof(uint8_t);
    cudaMalloc(&d_input, size);
    cudaMalloc(&d_output, size);

    cudaMemcpy(d_input, input, size, cudaMemcpyHostToDevice);

    dim3 block(16,16);
    dim3 grid((width + block.x - 1)/block.x, (height + block.y - 1)/block.y);

    blur_kernel<<<grid, block>>>(d_input, d_output, width, height, channels);

    cudaMemcpy(output, d_output, size, cudaMemcpyDeviceToHost);

    cudaFree(d_input);
    cudaFree(d_output);
}

}
