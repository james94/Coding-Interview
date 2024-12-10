cmake_minimum_required(VERSION 3.15...3.28)
project(terrain_tracker_range_sum_bst)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(terrain_navigation_tracker
    terrain_navigation_dem_tracker_bindings.cpp
)

target_compile_features(terrain_navigation_tracker PRIVATE cxx_std_20)

# Copy python script to build folder
add_custom_command(
    TARGET terrain_navigation_tracker POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/terrain_navigation_dem_tracker.py
    $<TARGET_FILE_DIR:terrain_navigation_tracker>/terrain_navigation_dem_tracker.py
)

install(TARGETS terrain_navigation_tracker DESTINATION .)
