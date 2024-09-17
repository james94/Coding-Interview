#include <iostream>
#include <vector>
#include <algorithm>

#include "rotate_array_kernel.cu"

using namespace std;

void cuda_rotate_array(vector<int>& nums, int k) {
    // If k is greater than the size of the array, we can just take the modulo
    k = k % nums.size();
    // Allocate memory on the GPU for the original array and result array
    int* d_nums;
    int* d_result;
    cudaMalloc(&d_nums, nums.size() * sizeof(int));
    cudaMalloc(&d_result, nums.size() * sizeof(int));

    // Copy the input array from host CPU to the GPU device
    cudaMemcpy(d_nums, nums.data(), nums.size() * sizeof(int), cudaMemcpyHostToDevice);
    
    // Define the number of threads per block and the number of blocks
    int threadsPerBlock = 256;
    int blocksPerGrid = (nums.size() + threadsPerBlock - 1) / threadsPerBlock;
    
    // Call the CUDA kernel to rotate the array
    rotateArrayKernel<<<blocksPerGrid, threadsPerBlock>>>(d_nums, d_result, nums.size(), k);

    // Copy the rotated array result from the GPU device back to the host CPU
    cudaMemcpy(nums.data(), d_result, nums.size() * sizeof(int), cudaMemcpyDeviceToHost);

    // Free the device memory
    cudaFree(d_nums);
    cudaFree(d_result);
}

void rotate_array_cuda_approach() {
    cout << "Rotate Array Approach 3: CUDA-based Rotation" << endl;
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    int k1 = 3;
    cuda_rotate_array(nums1, k1);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;

    vector<int> nums2 = {-1, -100, 3, 99};
    int k2 = 2;
    cuda_rotate_array(nums2, k2);
    for (int i = 0; i < nums2.size(); i++) {
        cout << nums2[i] << " ";
    }
    cout << endl;
}

int main() {
    // CUDA-based Rotation Approach 3: using CUDA to rotate the array
    rotate_array_cuda_approach();

    return 0;
}
