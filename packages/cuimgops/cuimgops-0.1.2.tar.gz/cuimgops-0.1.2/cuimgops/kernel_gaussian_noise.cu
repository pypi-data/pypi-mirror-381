#include <cuda_runtime.h>
#include <stdint.h>
#include <curand_kernel.h>

extern "C" {

__global__ void gaussian_noise_kernel(uint8_t* image, int width, int height, int channels, float mean, float stddev, unsigned long seed) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x >= width || y >= height) return;

    int idx = (y * width + x) * channels;
    
    // Initialize CURAND
    curandState state;
    curand_init(seed + idx, 0, 0, &state);

    for (int c = 0; c < channels; ++c) {
        float noise = curand_normal(&state) * stddev + mean;
        int val = (int)image[idx + c] + (int)noise;
        if (val < 0) val = 0;
        if (val > 255) val = 255;
        image[idx + c] = (uint8_t)val;
    }
}

void add_gaussian_noise(uint8_t* image, int width, int height, int channels, float mean, float stddev) {
    uint8_t *d_image;
    size_t size = width * height * channels * sizeof(uint8_t);
    cudaMalloc(&d_image, size);
    cudaMemcpy(d_image, image, size, cudaMemcpyHostToDevice);

    dim3 block(16,16);
    dim3 grid((width + block.x - 1)/block.x, (height + block.y - 1)/block.y);

    gaussian_noise_kernel<<<grid, block>>>(d_image, width, height, channels, mean, stddev, 1234UL);

    cudaMemcpy(image, d_image, size, cudaMemcpyDeviceToHost);
    cudaFree(d_image);
}

}
