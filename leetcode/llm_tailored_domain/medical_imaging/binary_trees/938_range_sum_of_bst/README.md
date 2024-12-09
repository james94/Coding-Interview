# 938. Range Sum of BST (Medical Imaging)

Leetcode Reference Original Problem: https://leetcode.com/problems/range-sum-of-bst/description/

Perplexity AI updated wording of leetcode question tailoring for medical imaging: https://www.perplexity.ai/search/you-are-a-software-infrastruct-AfXf_DZdRAKTJGnQ7rnuwA

## Overview

### Identify & Quantify Brain Region of Interest Intensity Levels

You are developing a medical imaging software for analyzing brain MRI scans. The software uses a binary tree data structure to represent the hierarchical segmentation of brain regions. Each node in the tree represents a brain region, with the value indicating the region's average pixel intensity.

Design and implement a C++20 function that, given the root node of this binary tree and two intensity thresholds (low and high), returns the sum of average intensities for all brain regions with intensities falling within the inclusive range [low, high]. This function will be used to identify and quantify regions of interest in the brain based on their intensity levels.

Your implementation should consider the following:

1. Efficient traversal of the binary tree
2. Proper handling of edge cases
3. Time and space complexity analysis
4. Potential for parallelization to improve performance on large datasets
5. Error handling and input validation
6. Unit testing strategy

## Example:

~~~bash
Input: root = [100,50,150,30,70,null,180], low = 70, high = 150
Output: 320
Explanation: Brain regions with intensities 70, 100, and 150 are in the range [70, 150]. 70 + 100 + 150 = 320.
~~~


## Constraints:

- The number of nodes in the tree is in the range [1, 2 * 10^6].
- 1 <= Node.intensity <= 1000
- 1 <= low <= high <= 1000
- All Node.intensity values are unique.

Provide a detailed explanation of your approach, including any design patterns or C++20 features you would use to enhance the solution's efficiency and readability.
