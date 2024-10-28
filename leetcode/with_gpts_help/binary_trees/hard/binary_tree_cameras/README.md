# 968. Binary Tree Cameras

**Leetcode Binary Tree Questions**:

- https://leetcode.com/problem-list/binary-tree/

**Leetcode Problem:**

- https://leetcode.com/problems/binary-tree-cameras/description/?envType=problem-list-v2&envId=binary-tree

**ChatGPT Solution:**

- https://chatgpt.com/share/670339a2-058c-8005-ba2a-fb2866287aa1

**OBJECTIVE:**

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

**CONSTRAINTS:**

- The number of nodes in the tree is in the range [1, 1000].
- Node.val == 0

**EXAMPLES:**

Example 1:

~~~bash
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
~~~

Example 2:

~~~bash
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
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
