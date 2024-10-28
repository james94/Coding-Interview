cmake_minimum_required(VERSION 3.5)

find_package(GTest REQUIRED)

enable_testing()

# Use Hash Set similar to Hash Table to simplify path
add_executable(asteroid_collision_tests main.cpp)

target_link_libraries(asteroid_collision_tests GTest::GTest GTest::Main)

add_test(NAME asteroid_collision_tests COMMAND asteroid_collision_tests)
