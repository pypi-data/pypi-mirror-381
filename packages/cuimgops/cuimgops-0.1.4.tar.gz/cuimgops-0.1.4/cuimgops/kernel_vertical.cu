#include <cuda_runtime.h>
#include <stdint.h>

extern "C" {

__global__ void vertical_flip_kernel_shared(const uint8_t* input, uint8_t* output, int width, int height, int channels) {
    extern __shared__ uint8_t tile[];

    int tx = threadIdx.x;
    int ty = threadIdx.y;
    int x  = blockIdx.x * blockDim.x + tx;
    int y  = blockIdx.y * blockDim.y + ty;

    int local_idx = (ty * blockDim.x + tx) * channels;

    if (x < width && y < height) {
        // Load pixel into shared memory
        for (int c = 0; c < channels; ++c) {
            tile[local_idx + c] = input[(y * width + x) * channels + c];
        }
    }

    __syncthreads();

    if (x < width && y < height) {
        // Global vertical flip index
        int flipped_y = height - 1 - y;
        for (int c = 0; c < channels; ++c) {
            output[(flipped_y * width + x) * channels + c] = tile[local_idx + c];
        }
    }
}

void vertical_flip(uint8_t* input, uint8_t* output, int width, int height, int channels) {
    uint8_t *d_input, *d_output;
    size_t size = width * height * channels * sizeof(uint8_t);
    cudaMalloc(&d_input, size);
    cudaMalloc(&d_output, size);

    cudaMemcpy(d_input, input, size, cudaMemcpyHostToDevice);

    dim3 block(16, 16);
    dim3 grid((width + block.x - 1)/block.x,
              (height + block.y - 1)/block.y);

    size_t sharedMemSize = block.x * block.y * channels * sizeof(uint8_t);

    vertical_flip_kernel_shared<<<grid, block, sharedMemSize>>>(d_input, d_output, width, height, channels);

    cudaMemcpy(output, d_output, size, cudaMemcpyDeviceToHost);

    cudaFree(d_input);
    cudaFree(d_output);
}

}