# Binary Trees: 449. Serialize and Deserialize BST

**Leetcode Binary Tree Questions**:

- https://leetcode.com/problem-list/binary-tree/

**Leetcode Problem:**

- https://leetcode.com/problems/serialize-and-deserialize-bst/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM

**ChatGPT Solution:**

- https://chatgpt.com/share/67031379-b4a4-8005-85da-8643daac83ff

**OBJECTIVE:**

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

**CONSTRAINTS:**

- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The input tree is guaranteed to be a binary search tree.

**EXAMPLES:**

Example 1:

~~~bash
Input: root = [2,1,3]
Output: [2,1,3]
~~~

Example 2:

~~~bash
Input: root = []
Output: []
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

