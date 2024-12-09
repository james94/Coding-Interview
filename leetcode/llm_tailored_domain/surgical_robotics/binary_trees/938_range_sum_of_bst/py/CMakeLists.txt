cmake_minimum_required(VERSION 3.15...3.28)
project(surgical_tracker_range_sum_bst)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(surgical_instrument_tracker
    surgical_instrument_tracker_bindings.cpp
)

target_compile_features(surgical_instrument_tracker PRIVATE cxx_std_20)

# target_include_directories(
#     surgical_instrument_tracker ./
# )

# Copy python script to build folder
add_custom_command(
    TARGET surgical_instrument_tracker POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/surgical_instrument_tracker.py
    $<TARGET_FILE_DIR:surgical_instrument_tracker>/surgical_instrument_tracker.py
)

install(TARGETS surgical_instrument_tracker DESTINATION .)

# add_executable(${PROJECT_NAME} main.cpp)
