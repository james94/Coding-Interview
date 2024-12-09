# 938. Range Sum of BST (Surgical Robotics)

Leetcode Reference Original Problem: https://leetcode.com/problems/range-sum-of-bst/description/

Perplexity AI updated wording of leetcode question tailoring for surgical robotics: https://www.perplexity.ai/search/you-are-a-software-infrastruct-kVPdzVQ.SkOL5o3vZYP6Kw

## Overview

### Surgical Instrument Tracking System

You are developing a software system for tracking surgical instruments during robotic surgery.
The system uses a binary search tree to represent the positions of various instruments in the
surgical field.
Each node in the tree represents an instrument, with its value corresponding to its distance
from a reference point in millimeters.

Your task is to implement a function that calculates the total number of movements made by
instruments within a specified range during a surgical procedure.

### Problem Statement

Given the root node of a binary search tree representing surgical instrument positions and two integers
`min_distance` and `max_distance`, return the sum of movement counts for all instruments with
distances in the inclusive range [`min_distance`, `max_distance`].

## Example

~~~bash
Input: 
root = [100,50,150,30,70,null,180] (representing instrument distances in mm)
min_distance = 70
max_distance = 150

Output: 320
Explanation: Instruments at distances 70, 100, and 150 mm are in the range [70, 150]. 
             Their movement counts are 70 + 100 + 150 = 320.
~~~

## Constraints

- The number of instruments (nodes) in the tree is in the range [1, 2 * 10^4]
- 1 <= Node.value (instrument distance) <= 10^5
- 1 <= Nmin_distance <= max_distance <= 10^5
- All Node.value are unique

## Additional Requirements

1\. Implement the solution in C++20, focusing on performance and memory efficiency.

2\. Provide a detailed analysis of the time and space complexity of your solution.

3\. Discuss how your implementation would scale for larger surgical datasets and potential
optimizations.

4\. Consider thread safety in your design, as the tracking system may be accessed by
multiple threads simultaneously.

5\. Explain how you would extend this system to handle real-time updates of instrument
positions during surgery.
