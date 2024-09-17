# 189. Rotate Array

Link References:

**Leetcode Problem:**

- https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

**ChatGPT solution:**

- https://chatgpt.com/share/66e69e8b-9230-8005-a527-8a34bdf74fa6

**OBJECTIVE:** given an integer array `nums`, rotate the array to right by `k` steps where `k` is non-negative.

**CONSTRAINTS:**

~~~bash
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
~~~

**FOLLOW UP:**

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.

Could you do it in-place with O(1) extra space?

**EXAMPLES:**

Example 1:

~~~bash
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
~~~

Example 2:

~~~bash
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
~~~

## Solution

~~~bash
pushd cpp
mkdir build
pushd build

cmake ..
make -j $(nproc)

popd # exit build/
popd # exit cpp
~~~

Output:

~~~bash
# pushd cpp/build
# ./rotate_array 

Rotate Array Approach 1: Multi-Reverses Rotation
5 6 7 1 2 3 4 
3 99 -1 -100 
Rotate Array Approach 2: Cyclic Replacements Rotation
5 6 7 1 2 3 4 
3 99 -1 -100 

# ./run_gpu_rotate_array 

Rotate Array Approach 3: CUDA-based Rotation
5 6 7 1 2 3 4 
3 99 -1 -100 
~~~
