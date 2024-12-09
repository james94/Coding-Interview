# 938. Range Sum of BST (Unmanned Aircraft Systems)

Leetcode Reference Original Problem: https://leetcode.com/problems/range-sum-of-bst/description/

Perplexity AI updated wording of leetcode question tailoring for Unmanned Aircraft Systems: https://www.perplexity.ai/search/you-are-a-software-infrastruct-TMl9mIiWR9eHPLRY43_2lw

## Overview

### Terrain Navigation System

You are developing a terrain-referenced navigation system for a UAS using a binary search tree
to store elevation data. The tree represents a Digital Elevation Model (DEM) where each node contains the elevation value for a specific geographic coordinate. Given the root node of this binary search tree and two elevation thresholds
(low and high), implement a function that calculates the sum of all elevation values within the inclusive range 
[low, high].

This function will be crucial for terrain-following algorithms and obstacle avoidance systems in the UAS
software infrastructure.

## Example 1

~~~bash
Input: 
DEM root = [100,50,150,30,70,null,180] (elevations in mm)
low = 70
high = 150

Output: 320
Explanation: Elevation ponits 70, 100, and 150 m are within the range [70, 150]. 
            70 + 100 + 150 = 320.
~~~

## Example 2

~~~bash
Input: 
DEM root = [100,50,150,30,70,130,180,10,null,60] (elevations in mm)
low = 60
high = 100

Output: 230
Explanation: Elevation ponits 60, 70, and 100 m are within the range [60, 100]. 
            60 + 70 + 150 = 320.
~~~

## Constraints

- The number of nodes in the DEM tree is in the range [1, 2 * 10^4]
- 1 <= Node.elevation  <= 10^5 (in meters)
- 1 <= low <= high <= 10^5 (in meters)
- All Node.elevation are unique

## Additional Requirements

1\. Implement the solution in C++20 features where applicable.

2\. Analyze and optimize the time and space complexity of your solution.

3\. Consider the scability of your approach for larger DEMs and frequent queries

4\. Discuss how this function could be integrated into a real-time UAS navigation system.

5\. Explain how you would handle potential errors or edge cases in a production environment.
