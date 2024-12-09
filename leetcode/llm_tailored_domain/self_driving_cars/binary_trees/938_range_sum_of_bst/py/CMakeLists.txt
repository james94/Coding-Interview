cmake_minimum_required(VERSION 3.15...3.28)
project(sdc_safety_tracker_range_sum_bst)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(sdc_safety_score_tracker
    sdc_safety_score_tracker_bindings.cpp
)

target_compile_features(sdc_safety_score_tracker PRIVATE cxx_std_20)

# Copy python script to build folder
add_custom_command(
    TARGET sdc_safety_score_tracker POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/sdc_safety_score_tracker.py
    $<TARGET_FILE_DIR:sdc_safety_score_tracker>/sdc_safety_score_tracker.py
)

install(TARGETS sdc_safety_score_tracker DESTINATION .)
