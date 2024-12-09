# 938. Range Sum of BST (Self-Driving Cars)

Leetcode Reference Original Problem: https://leetcode.com/problems/range-sum-of-bst/description/

Perplexity AI updated wording of leetcode question tailoring for self-driving cars: https://www.perplexity.ai/search/you-are-a-software-infrastruct-XcBWj2OAS.GoOQ7mmh154g

## Overview

### Self-Driving Car Safety Score System

Given a binary tree representing a hirearchical decision-making system for a self-driving car, where each node contains a safety score (integer value) for a specific driving action, implement a function that calculates the total safety score for actions within a specified range. The function should take the root node of the binary tree and two integers, `min_threshold` and `max_threshold`, as input and return the sum of safety scores for all nodes with values in the inclusive rnage [`min_threshold`, `max_threshold`]. 

## Example

~~~bash
Input: 
root = [10,5,15,3,7,180] (representing safety score for a specific driving action)
min_threshold = 7
max_threshold = 15

Output: 32
Explanation: Nodes with SDC safety scores 7, 10, and 15 are in the range [7, 15]. 
             The total SDC safety score is 7 + 10 + 15 = 32.
~~~

## Constraints

- The number of SDC safety scores (nodes) in the tree is in the range [1, 2 * 10^4]
- 1 <= Node.value (SDC safety score) <= 10^5
- 1 <= Nmin_threshold <= max_threshold <= 10^5
- All Node.value are unique

## Additional Requirements

Implement the calculateSafetyScore function, considering the following:

1. Optimize for both time and space complexity.
2. Consider edge cases and error handling.
3. Discuss how this algorithm could be integrated into a larger self-driving car system.
4. Explain how you would ensure thread-safety if this function were to be called concurrently by multiple decision-making modules.
