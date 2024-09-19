#include <iostream>
#include <vector>
#include <stack>
#include <gtest/gtest.h>

// TODO: Try to create a MiNIFi C++ processor for leetcode function

// ChatGPT: https://chatgpt.com/share/66eb04ae-0730-8005-a04e-23408867177b

// Perplexity.ai: https://www.perplexity.ai/search/which-leetcode-stack-medium-qu-e6Xq3us.Saqv6nusltOXRg

std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
    std::stack<int> stack_asteroids;

    for(int ast : asteroids) {
        bool exploded = false;

        // std::cout << "Current asteroid: " << ast << std::endl;

        // Collision can happen only if current asteroid is moving left
        // and the stack's top asteroid is moving right.
        while (!stack_asteroids.empty() && ast < 0 && stack_asteroids.top() > 0) {
            // std::cout << "Stack top asteroid: " << stack_asteroids.top() << std::endl;
            // Compare sizes
            if (stack_asteroids.top() < -ast) {
                // Top of the stack asteroid explodes
                stack_asteroids.pop();
            }
            else if (stack_asteroids.top() == -ast) {
                // Both asteroids explode
                stack_asteroids.pop();
                exploded = true;
                break;
            }
            else {
                // Current asteroid explodes
                exploded = true;
                break;
            }
        }

        // If no explosion, push the current asteroid onto the stack
        if (!exploded) {
            stack_asteroids.push(ast);
        }
    }

    // Extract the remaining asteroids from the stack
    std::vector<int> result(stack_asteroids.size());
    for (int i = stack_asteroids.size() - 1; i >= 0; i--) {
        result[i] = stack_asteroids.top();
        stack_asteroids.pop();
    }

    return result;
}

void printVector(std::vector<int>& vec) {
    for (int a : vec) {
        std::cout << a << " ";
    }
    std::cout << std::endl;
}

void runAsteroidCollisionExamples() {
    // Example 1
    std::vector<int> asteroids1 = {5, 10, -5};
    std::vector<int> remaining_asteroids1 = asteroidCollision(asteroids1);

    printVector(remaining_asteroids1);

    // Example 2
    std::vector<int> asteroids2 = {8, -8};
    std::vector<int> remaining_asteroids2 = asteroidCollision(asteroids2);

    printVector(remaining_asteroids2);

    // Example 3
    std::vector<int> asteroids3 = {10, 2, -5};
    std::vector<int> remaining_asteroids3 = asteroidCollision(asteroids3);

    printVector(remaining_asteroids3);
}

// Test Case 1: Example 1
TEST(AsteroidCollisionTest, Example1) {
    std::vector<int> asteroids1 = {5, 10, -5};
    std::vector<int> remaining_asteroids1 = asteroidCollision(asteroids1);

    std::vector<int> expected1 = {5, 10};
    ASSERT_EQ(remaining_asteroids1, expected1);
}

// Test Case 2: Example 2
TEST(AsteroidCollisionTest, Example2) {
    std::vector<int> asteroids2 = {8, -8};
    std::vector<int> remaining_asteroids2 = asteroidCollision(asteroids2);

    std::vector<int> expected2 = {};
    ASSERT_EQ(remaining_asteroids2, expected2);
}

// Test Case 3: Example 3
TEST(AsteroidCollisionTest, Example3) {
    std::vector<int> asteroids3 = {10, 2, -5};
    std::vector<int> remaining_asteroids3 = asteroidCollision(asteroids3);

    std::vector<int> expected3 = {10};
    ASSERT_EQ(remaining_asteroids3, expected3);
}


int main() {
    bool run_gtests = true;

    if (run_gtests) {
        testing::InitGoogleTest();
        return RUN_ALL_TESTS();
    }

    runAsteroidCollisionExamples();
    return 0;
}
