cmake_minimum_required(VERSION 3.15...3.28)
project(brain_region_range_sum_bst)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(brain_region_analysis
    brain_region_analysis_bindings.cpp
)

target_compile_features(brain_region_analysis PRIVATE cxx_std_20)

# target_include_directories(
#     brain_region_analysis ./
# )

# Copy python script to build folder
add_custom_command(
    TARGET brain_region_analysis POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/brain_region_analysis.py
    $<TARGET_FILE_DIR:brain_region_analysis>/brain_region_analysis.py
)

install(TARGETS brain_region_analysis DESTINATION .)

# add_executable(${PROJECT_NAME} main.cpp)
