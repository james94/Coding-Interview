# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#14
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Binary Tree Construction: Rebuild a tree using traversal sequences.
# - Recursion: split the problem into smaller subproblems by leveraging the
#   properties of preorder and inorder traversals
# - Hash Maps: Efficiently locate the root node's position in the inorder array
#
# Clarifying Questions:
#
# 1. Are the elements in the traversal arrays unique?
#   - Yes (constraints state "unique values")
#
# 2. How are the subtrees determined from the root?
#   - In inorder traversal, elements left of the root form the left subtree, and elements
#   right form the right subtree.
#
# Potential Solutions:
#
# 1. Brute Force: Repeatedly search for the root in the inorder array (O(n^2) time)
#
# 2. Optimized Approach: Use a hash map to store inorder indices for O(1) lookups, reducing
#   time complexity to O(n).
#
##
# While Coding
##
#
# Implementation we'll use O(n) Time Complexity, O(n) Space Complexity.
#
# Explanation of Solution:
#
# 1. Hash Map: inorder_map stores the indices of values in the inorder array for O(1) lookups.
# 
# 2. Recursive Helper:
#   - The root is always the current element in preorder (tracked by pre_idx)
#   - Split the inorder array into left and right subtrees based on the root's position.
#   - Recursively build the left and right subtrees using the updated boundaries.
#
##
# After Coding
##
#
# Potential Improvements:
#
# Time Complexity: O(n), as each node is processed once
#
# Space Complexity: O(n) for the hash map and O(h) for the recursion stack (h = tree height)
#
# Edge Cases:
#   - Single-node tree (preorder = [-1], inorder = [-1])
#   - Skewed trees (all nodes on the left/right).
from typing import List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Create a hash map to store value-to-index mappings for inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Use a list to track the current index in preorder (mutable)
        pre_idx = [0]

        def helper(in_start: int, in_end: int) -> TreeNode:
            if in_start > in_end:
                return None
            
            # Get the root value from preorder and increment the index
            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)
            pre_idx[0] += 1

            # Find the root's position in inorder
            root_pos = inorder_map[root_val]

            # Recursively build left and right subtrees
            root.left = helper(in_start, root_pos - 1)
            root.right = helper(root_pos + 1, in_end)

            return root
        
        return helper(0, len(inorder) - 1)

def print_tree(root: TreeNode) -> List[int]:
    # Helper to print the tree in level order (for testing)
    if not root:
        return []
    
    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)
        if node and (node.left or node.right):
            queue.append(node.left)
            queue.append(node.right)
    return result

def main():
    preorder1 = [3,9,20,15,7]
    inorder1 = [9,3,15,20,7]

    sol = Solution()
    tree1 = sol.buildTree(preorder1, inorder1)
    print(print_tree(tree1)) # Output: [3,9,20,None,None,15,7]

    preorder2 = [-1]
    inorder2 = [-1]
    tree2 = sol.buildTree(preorder2, inorder2)
    print(print_tree(tree2)) # Output: [-1]

if __name__ == "__main__":
    main()
    