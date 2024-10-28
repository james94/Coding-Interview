cmake_minimum_required(VERSION 3.5)

find_package(GTest REQUIRED)

enable_testing()

# Use Hash Set similar to Hash Table to simplify path
add_executable(simplify_path_tests main.cpp)

target_link_libraries(simplify_path_tests GTest::GTest GTest::Main)

add_test(NAME simplify_path_tests COMMAND simplify_path_tests)
