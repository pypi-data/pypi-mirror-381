#include <cuda_runtime.h>
#include <stdint.h>

extern "C" {

__global__ void horizontal_flip_kernel(const uint8_t* input, uint8_t* output, int width, int height, int channels) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height) {
        for (int c = 0; c < channels; ++c) {
            output[(y*width + x)*channels + c] = input[(y*width + (width - 1 - x))*channels + c];
        }
    }
}

void horizontal_flip(uint8_t* input, uint8_t* output, int width, int height, int channels) {
    uint8_t *d_input, *d_output;
    size_t size = width * height * channels * sizeof(uint8_t);
    cudaMalloc(&d_input, size);
    cudaMalloc(&d_output, size);

    cudaMemcpy(d_input, input, size, cudaMemcpyHostToDevice);

    dim3 block(16,16);
    dim3 grid((width + block.x - 1)/block.x, (height + block.y - 1)/block.y);
    horizontal_flip_kernel<<<grid, block>>>(d_input, d_output, width, height, channels);

    cudaMemcpy(output, d_output, size, cudaMemcpyDeviceToHost);

    cudaFree(d_input);
    cudaFree(d_output);
}

}
