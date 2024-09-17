# Hash Table: 128. Longest Consecutive Sequence

**Leetcode Hash Table Questions:**

- https://leetcode.com/problem-list/hash-table/

**Leetcode Problem:**

- https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=hash-table

**ChatGPT solution:**

- https://chatgpt.com/share/66e796dd-2f74-8005-aa4a-a12386fcfe25

**OBJECTIVE:**

Given an unsorted array of integers `nums`, return the ***length of the longest consecutive elements sequence.***

You must write an algorithm that runs in `O(n)` time.

**CONSTRAINTS:**

~~~bash
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
~~~

**FOLLOW UP:**

**EXAMPLES:**

Example 1:

~~~bash
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
~~~

Example 2:

~~~bash
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
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
# /find_longest_streak 

Vector nums1: 100 4 200 1 3 2 
Longest Consecutive Sequence in nums1: 4
Vector nums2: 0 3 7 2 5 8 4 6 0 1 
Longest Consecutive Sequence in nums2: 9
~~~
