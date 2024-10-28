#include <cuda_runtime.h>

__global__ void rotateArrayKernel(int* d_nums, int* d_result, int num_size, int k) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < num_size) {
        // Compute new index position to rotate to
        int new_rotate_pos = (idx + k) % num_size;
        // Store element into new position
        d_result[new_rotate_pos] = d_nums[idx];
    }
}
