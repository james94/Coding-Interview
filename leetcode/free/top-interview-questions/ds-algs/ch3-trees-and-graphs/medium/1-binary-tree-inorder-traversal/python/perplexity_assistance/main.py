from typing import List

# Perplexity Reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#3

# Data Structures & Algorithm Concepts
#
# Binary Trees: involves traversing a binary tree
# Depth-First Search: Inorder traversal is a form of DFS where we visit
# the left subtree, the current node, and then the right subtree
#
# Stacks: For an interative solution, a stack can be used to manage node sequences

##
# Explanation:
##
#
# Recursive Approach: visit the left subtree, append the current node's value, and then
# visit the right subtree
#
# Iterative Approach: Use a stack to store nodes. Traverse to the leftmost node, pop
# and append its value, then move to its right child
#
# Time Complexity: Both solutions have a time complexity of O(n), where "n" is the number
# of nodes in the tree
#
# Space Complexity: The recursive solution has a space complexity of O(h), where "h" is
# the height of the tree (worst case O(n) for skewed trees). The iterative solution also
# has a space complexity of O(h) due to stack.
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        result = []

        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                result.append(node.val)
                inorder_helper(node.right)
        
        inorder_helper(root)
        return result

    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result

def main():
    tree = TreeNode(1)
    tree.left = None
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    soln = Solution()
    # recursive_inorder_res = soln.inorderTraversalRecursive(tree)
    recursive_inorder_res = soln.inorderTraversalIterative(tree)

    print(recursive_inorder_res)

if __name__ == "__main__":
    main()
