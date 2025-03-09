# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#21
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Binary Search Tree (BST): Nodes are ordered such that left subtree values are less than the root, and right subtree
#   values are greater.
#
# - In-Order Traversal: Visits nodes in ascending order
#
# - Iterative Approach with Stack: Allows early termination once the kth element is found.
#
# Clarifying Questions:
#
# 1. Are node values unique?
#   - Yes, BSTs typically have unique values, though the problem doesn't explicitly state this. The
#       examples suggest unique values.
#
# 2. What if the tree is modified frequently?
#   - For the follow-up, consider augmenting nodes with subtree counts for efficient queries
#
# Potential Solutions:
#
# 1. Recursive In-Order Traversal: Collect all elements and return the kth element. (O(n) time and space)
#
# 2. Iterative In-Order Traversal: Traverse nodes iteratively and stop at the kth element (O(k + h) time, O(h) space)
#
# 3. Augmented BST (Follow-Up): Store subtree counts in nodes for O(h) time queries after O(n) processing.
#
##
# While Coding
##
#
# Implementation we'll use Iterative In-Order Traversal
#
# Explanation of Solution:
#
# 1. Stack Initialization: Use a stack to simulate the recursive call stack for in-order traversal
#
# 2. Leftmost Traversal: Push all left nodes onto the stack until reaching the smallest element
#
# 3. Node Processing: Pop nodes from the stack (ascending order), decrement k. When k == 0, return the current node's value.
#
# 4. Right Subtree Handling: After processing a node, move to its right subtree to continue traversal
#
##
# After Coding
##
#
# Time Complexity: O(h + k), where h is the tree height. Worst case (skewed tree): O(n)
#
# Space Complexity: O(h) for the stack. Worst case: O(n)
#
# Potential Improvements:
#
# To optimize for frequent updates and queries:
#
#   - Augmented Nodes: Store the size of the left subtree in each node
#   - Modified Insert/Delete: Update subtree counts during modification
#   - Optimized Search: During queries, compare k with the left subtree size to determine the search path (left/current/right)
#
# Edge Cases:
#
# - k = 2: Return the smallest element (leftmost node)
# - k = n: Return the largest element (rightmost node)
# - Single-node tree: Return the node's value
#

## 
# Summary
##
#
# To solve the Kth Smallest Element in a BST problem, we'll use an iterative in-order traversal
# approach. This method efficiently finds the kth smallest element by leveraging the BSTs property
# that in-order traversal yields nodes in ascending order.
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root

        while True:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the smallest node
            current = stack.pop()
            k -= 1

            if k == 0:
                # Found kth smallest node
                return current.val

            # Move to the right subtree
            current = current.right

def main():
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)

    print(Solution().kthSmallest(root1, 1)) # Output 1

    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    print(Solution().kthSmallest(root2, 3)) # Output 3

if __name__ == "__main__":
    main()
