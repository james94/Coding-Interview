#include <iostream>
#include <vector>

using namespace std;

/*
**Leetcode Binary Tree Questions**:

- https://leetcode.com/problem-list/binary-tree/

**Leetcode Problem:**

- https://leetcode.com/problems/binary-tree-cameras/description/?envType=problem-list-v2&envId=binary-tree

**ChatGPT Solution:**

- https://chatgpt.com/share/670339a2-058c-8005-ba2a-fb2866287aa1
*/

/*
Software Design Perspective

- We aim to cover all nodes in a binary tree with the minimum
number of cameras.
- Each camera can monitor its parent, itself and its immediate children.
- The design must be efficient given the constraints with up to 1000 nodes in the tree.
- We break down the problem by focusing on a greedy algorithm approach
that minimizes camera placement while ensuring full coverage of the tree.
    - This is a tree traversal problem and a bottom-up post-order traversal is
    particularly useful here because decisions on camera placement can be
    optimized from the leaf nodes upwards to the root.

Approach:

- 1. State 0: The node needs a camera
- 2. State 1: The node has a camera
- 3. State 2: The node is monitored by a camera, but doesn't need a camera itself

Using post-order traversal (left-right-root), we process each node and its children.
If a child node is not covered (State 0), we place a camera at the current node.
If a child node is covered (State 2), we may skip placing a camera. This approach ensures
minimum camera placement.

Time Complexity:
- O(n) where n is the number of nodes in the tree. Each node is visited once during the post-order traversal.

Space Complexity:
- O(h) where h is the height of the tree due to the recursive stack space.
    In the worst case, the tree is skewed and the space complexity is O(n).
*/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int minCameraCover(TreeNode* root) {
        // If root needs a camera, add one
        if (dfs(root) == 0) {
            cameras++;
        }

        return cameras;
    }

    // Helper function for post-order traversal
    int dfs(TreeNode* node) {
            // If node is NULL, its considered covered
        if (!node) {
            return 2;
        }

        int left = dfs(node->left);
        int right = dfs(node->right);

        // If either child is not covered, place a camera at this node
        if (left == 0 || right == 0) {
            cameras++;
            return 1; // This node has a camera
        }

        // If either child has a camera, this node is covered
        if (left == 1 || right == 1) {
            return 2; // This node is covered
        }

        // If both children are covered but have no camera
        return 0; // This node needs a camera
    }

private:
    int cameras = 0;
};

int main () {
    Solution solution;

    // Example 1
    TreeNode* root1 = new TreeNode(0);
    root1->left = new TreeNode(0);
    root1->left->left = new TreeNode(0);
    root1->left->right = new TreeNode(0);
    cout << "Minimum cameras needed for Example 1: " << solution.minCameraCover(root1) << endl;

    // Example 2
    TreeNode* root2 = new TreeNode(0);
    root2->left = new TreeNode(0);
    root2->left->left = new TreeNode(0);
    root2->left->left->right = new TreeNode(0);
    root2->left->left->right->left = new TreeNode(0);
    cout << "Minimum cameras needed for Example 2: " << solution.minCameraCover(root2) << endl;

    return 0;
}