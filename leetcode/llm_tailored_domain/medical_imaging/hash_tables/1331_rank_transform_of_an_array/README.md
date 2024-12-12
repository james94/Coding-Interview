# 1331. Rank Transform of an Array (Medical Imaging)

Leetcode Reference Original Problem: https://leetcode.com/problems/rank-transform-of-an-array/description/

Perplexity AI updated wording of leetcode question tailoring for medical imaging: https://www.perplexity.ai/search/you-are-a-software-infrastruct-1T73.QI7TrGVBVjp0uB9dg

## Overview

### MRI Signal Intensity Ranking

In MRI image processing, you are tasked with developing a software module to rank voxel intensities in a 3D MRI volume. This ranking is crucial for various post-processing techniques, including image segmentation and feature extraction.

Given a 3D array `voxel_intensities` representing the signal intensities of an MRI volume, replace each voxel's intensity with its rank. The rank represents the relative strength of the MRI signal at that location.

Implement a function `rank_transform(voxel_intensities)` that follows these requirements:

1. Rank is an integer starting from 1.
2. Higher signal intensities receive higher ranks
3. Equal intensities must have the same rank.
4. Ranks should be as compact as possible (no skipped numbers).

Your implement should consider the following:

- Optimize for both time and space complexity, considering that MRI volumes can be large (e.g., 256x256x128 voxels)

- Design your solution to be thread-safe, as it may be used in a multi-threaded environment.

- Implement error handling for edge cases, such as empty or malformed input.

## Example 1

~~~bash
Input: voxel_intensities = [40, 10, 20, 30]
Output: [4, 1, 2, 3]
Explanation: 40 is the highest intensity, 10 is the lowest, 20 is the second lowest, and 30 is the third lowest.
~~~

## Example 2

~~~bash
Input: voxel_intensities = [100, 100, 100]
Output: [1, 1, 1]
Explanation: Equal intensities share the same rank.
~~~

## Example 3

~~~bash
Input: voxel_intensities = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

~~~


## Constraints:

- 0 <= voxel_intensities.size() <= 10^6
- -10^9 <= voxel_intensities[i] <= 10^9
