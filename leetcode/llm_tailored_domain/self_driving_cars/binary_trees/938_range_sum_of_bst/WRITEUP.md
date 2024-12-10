# 938. Range Sum of BST (Self-Driving Cars) Solution

## Software Design Perspective

To solve this problem, we'll use a depth-first search (DFS) approach to traverse the binary tree. We'll implement
the `calculateSafetyScore` function recursively, which will allow us to efficiently explore all nodes in the tree while keeping track of the safety scores within the specified range.

## Time Complexity

- O(N) where N is the number of nodes in the tree. We visit each node exactly once.

## Space Complexity

- O(H) where H is the height of the tree. This is due to the recursive call stack in the worst case. In the worst case (skewed
tree), it could be O(N), but for a balanced BST, it would be O(logN)

## C++ Implementation

Refer to [cpp/main.cpp](./cpp/main.cpp) for C++ implementation.

## Methodology

1\. Optimization: The solution is optimized for both time and space complexity. It uses a single tree traversal
and minimal additional space.

2\. Edge cases and error handling: The function checks for invalid input (min_threshold > max_threshold) and throws
an exception. It also handles null nodes gracefully.

3\. Integration into a larger self-driving car system: This algorithm could be part of a decision-making module
that evaluates various driving actions based on their safety scores. The binary tree structure could represent
a hierarchy of decisions, with each node representing a specific action or sub-decision.

4\. Thread-safety: The `SafetyScoreCalculator` class uses a mutex to ensure thread-safety when called concurrently
by multiple decision-making modules. The `lock_guard` is used to automatically lock and unlock the mutex.

## Run C++ Solution

~~~bash
cd cpp

mkdir build

cmake ..
make

./sdc_safety_range_sum_bst

cd ..
~~~

## Run PyBind Solution

~~~bash
cd py

mkdir build

cmake ..
make

python3 sdc_safety_score_tracker.py

cd ..
~~~

## Resource

Perplexity AI updated wording of leetcode question tailoring for self-driving cars, also includes the solution and other important links: https://www.perplexity.ai/search/you-are-a-software-infrastruct-XcBWj2OAS.GoOQ7mmh154g

## Citations

- [1] https://www.atlantis-press.com/article/125980543.pdf
- [2] https://www.reddit.com/r/SelfDrivingCars/comments/iie3qs/preparing_for_a_c_software_engineer_for_self/
- [3] https://neptune.ai/blog/self-driving-cars-with-convolutional-neural-networks-cnn
- [4] https://igotanoffer.com/blogs/tech/google-software-engineer-interview
- [5] https://www.diva-portal.org/smash/get/diva2:907048/FULLTEXT01.pdf
- [6] https://www.upgrad.com/blog/project-ideas-in-cplusplus-for-beginners/
- [7] https://www.thinkautonomous.ai/blog/deep-learning-in-self-driving-cars/
