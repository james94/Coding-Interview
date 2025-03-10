# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#27

##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Binary Tree Traversal: We need to traverse the tree level by level
# - Breadth-First Search (BFS): BFS is ideal for level-order traversal using a queue
# - Zigzag Pattern: Alternate the order of nodes at each level (left-to-right, then right-to-left)
# - Deque: A double-ended queue can help efficiently append elements in reverse order
#
##
# Clarifying Questions:
##
#
# 1. What should we return if the tree is empty?
#   - Return an empty list ([])
#
# 2. How do we handle single-node trees?
#   - The output should be a list with one sublist containing the single node value
#
# 3. Are negative values allowed in the tree?
#   - Yes, constraints allow values between -100 and 100.
#

# Potential Solutions:
#
# 1. Breadth-First Search (BFS):
#   - Use a queue to traverse the tree level by level
#   - Alternate the order of appending nodes at each level
#
# 2. Depth-First Search (DFS):
#   - Use recursion to traverse the tree, keeping track of levels and
#       reversing order as needed

##
# After Coding
##
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
#   - Each node is visited once.
#
# Space Complexity: O(n) for the queue and result storage
#
##
# Potential Improvements:
##
#
# 1. DFS Approach:
#   - Use recursion to traverse levels and maintain a list of lists for results
#   - Reverse lists at alternate levels after traversal
#
# 2. In-Place Reversal:
#   - Instead of using a deque, reverse lists at alternate levels before
#       appending to results
#

# Edge Cases:
#
# 1. Empty Tree (root = None): Return []
#
# 2. Single-Node Tree (root = ): Return []
#
# 3. Tree with only left or right children: Ensure zigzag alternates correctly

##
# While Coding:
##
#
# Explanation of BFS Approach:
#
# 1. Initialization:
#   - Use a deque for BFS traversal
#   - Maintain a left_to_right flag to alternate between normal and reverse order
#
# 2. Level Traversal:
#   - For each level, process all nodes in the queue.
#   - Append values to level_nodes (a deque) either normally (append) or in
#       reverse order (appendleft)
#
# 3. Toggle Direction:
#   - After processing each level, toggle the left_to_right flag.
#
# 4. Add Results:
#   - Convert level_nodes (a deque) to a list and add it to result
#

from collections import deque
from typing import List, Optional

##
# Summary
##
#
# This solution efficiently handles zigzag traversal using BFS with a deque
# for flexible appending. It alternates directions at each level and ensures optimal
# performance for trees up to the given constraints.
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root]) # Initialize queue with the root node
        left_to_right = True # Flag to track zigzag direction

        while queue:
            level_size = len(queue)
            level_nodes = deque() # Use deque to efficiently append elements in reverse order

            for _ in range(level_size):
                node = queue.popleft()

                # Append node value based on zigzag direction
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Convert the deque to list and add to result
            result.append(list(level_nodes)) 

            # Toggle direction for next level
            left_to_right = not left_to_right
        
        return result

def main():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while i < len(values):
            current = queue.popleft()

            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        
        return root

    sol = Solution()

    # Test Case 1
    list1 = [3,9,20,None,None,15,7]
    root1 = build_tree(list1)

    # Output: [[3],[20,9],[15,7]]
    print(sol.zigzagLevelOrder(root1))

    # Test Case 2
    list2 = [1]
    root2 = build_tree(list2)

    # Output: [[1]]
    print(sol.zigzagLevelOrder(root2))

    list3 = []
    root3 = build_tree(list3)

    # Output: []
    print(sol.zigzagLevelOrder(root3))

if __name__ == "__main__":
    main()
