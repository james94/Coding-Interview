# 82. Remove Duplicates from Sorted List II

Link References:

**Leetcode Problem:**

- https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

**ChatGPT solution:**

- https://chatgpt.com/share/66e783f0-9b74-8005-8550-12e839f0fed2

**OBJECTIVE:**

Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

**CONSTRAINTS:**

- The number of nodes in the list is in the range `[0, 300]`.

~~~bash
-100 <= Node.val <= 100
~~~

- The list is guaranteed to be sorted in ascending order.

**EXAMPLES:**

Example 1:

~~~bash
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
~~~

Example 2:

~~~bash
Input: head = [1,1,1,2,3]
Output: [2,3]
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
# ./remove_duplicates_llist 

Original List: 1 2 3 3 4 4 5 
List after Removing Duplicates: 1 2 5
~~~
