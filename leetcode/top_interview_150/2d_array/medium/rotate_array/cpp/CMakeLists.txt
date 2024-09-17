cmake_minimum_required(VERSION 3.5)

project(rotate_array LANGUAGES CXX CUDA)

# CPU Rotate Array executable
add_executable(rotate_array main.cpp)

####
#   GPU Rotate Array executable
####

# Find CUDA package (optional with modern CMake, but helps with older versions)
find_package(CUDA REQUIRED)

set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS} "-std=c++11")

cuda_add_library(gpu_rotate_array SHARED rotate_array_kernel.cu)

add_executable(run_gpu_rotate_array gpu_main.cu)

target_link_libraries(run_gpu_rotate_array gpu_rotate_array)
