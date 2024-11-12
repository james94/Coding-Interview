#include <iostream>
#include <vector>

// Time: 10:24PM - 10:58PM:

// Given the root of a binary tree, return the inorder
// traversal of its nodes' values.

// Binary Tree Traversal Algorithm (mainly referred to DFS English Pseudocde Word Reference):
    // https://en.wikipedia.org/wiki/Tree_traversal

// 94. Binary Tree Inorder Traversal
// Leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=company&envId=google&favoriteSlug=google-six-months&difficulty=EASY

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {

    }
    TreeNode(int x, TreeNode *left, TreeNode *right) :
        val(x), left(left), right(right) {

    }
};

class Solution {
public:
    // DFS: the search is deepened as much as possible before going to the next sibling
        // We perform these operations at each node
        // 1. If the current node is empty, then return
        // 2. Execute the following three operations in a certain order (inorderTraversal) LNR
            // L: Recursively traverse the current node's left subtree
            // N: Visit the current node value
            // R: Recursively travese the current node's right subtree
    std::vector<int> inorderTraversal(TreeNode *root) {

        if (root == nullptr) {
            return traversal_res;
        }

        // L: Recursively traverse current node's left subtree
        inorderTraversal(root->left);
        // N: Visit the current node
        std::cout << "root->val = " << root->val << std::endl;
        traversal_res.push_back(root->val);
        // R: Recursively traverse the current node's right subtree
        inorderTraversal(root->right);
        return traversal_res;
    }

    std::vector<int> traversal_res;
};

int main() {

    // Example 1: int root[] = {1, null, 2, 3}
    TreeNode *root_node1 = new TreeNode();

    root_node1->val = 1;
    root_node1->left = nullptr;
    root_node1->right = new TreeNode();
    root_node1->right->val = 2;
    root_node1->right->left = new TreeNode();
    root_node1->right->left->val = 3;

    // Example 1 Res: [1,3,2]
    Solution soln;
    std::cout << "Binary Tree DFS: Inorder Traversal:\n";
    std::vector<int> inorder_res = soln.inorderTraversal(root_node1);

    // Example 2: int root[] = {1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9}
    // TreeNode *root_node2 = new TreeNode();

    return 0;
}
