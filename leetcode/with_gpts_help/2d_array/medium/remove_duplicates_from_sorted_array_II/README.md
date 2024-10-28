# 80. Remove Duplicates from Sorted Array II

Link References:

**Leetcode Problem:**

- https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

**Perplexity.ai solution:**

- https://www.perplexity.ai/search/you-are-a-coding-interview-ass-nORHwUVmThuH673K060Y4Q

**ChatGPT solution:**

- https://chatgpt.com/share/66e65181-0e8c-8005-961b-ed3de4257d94


**OBJECTIVE:** Given an integer array `nums` sorted **in non-decreasing order**,
remove some duplicates in-place, so each unique element appears
**at most twice.** The relative order should be kept the same.

You must have the result be placed in the **first part** of the array
`nums`. 

If there are `k` elements after removing the duplicates, then the first `k`
elements of `nums` should hold the final result.

Do **not** allocate extra space for another array. You must do this by
modifying the input array in-place with O(1) extra memory.

**CONSTRAINTS:**

~~~bash
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
~~~

Custom Judge:

The judge will test your solution with the following code:

~~~cpp
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
~~~

Example 1:

~~~bash
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
~~~

Example 2:

~~~bash
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
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
Result k1: 5, Modified Array: 1 1 2 2 3 
Result k2: 7, Modified Array: 0 0 1 1 2 3 3
~~~
