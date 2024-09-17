# Reverse Linked List II

Link References:

**Leetcode Problem:**

https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

**ChatGPT solution:**

- https://chatgpt.com/share/66e77d9d-0c50-8005-b015-74655772a4dd

**OBJECTIVE:**

Given the `head` of a singly linked list, two integers `left` and `right` where `left <= right`, reverse the nodes of the list from `left` to position `right`, and return the ***reversed list***.

**CONSTRAINTS:**

- The number of nodes in the list is `n`.

~~~bash
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
~~~

**FOLLOW UP:**

Could you do it in one pass?

**EXAMPLES:**

Example 1:

~~~bash
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
~~~

Example 2:

~~~bash
Input: head = [5], left = 1, right = 1
Output: [5]
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
# ./reverse_linked_list 

Original List: 1 2 3 4 5 
Reversed List: 1 4 3 2 5
~~~
