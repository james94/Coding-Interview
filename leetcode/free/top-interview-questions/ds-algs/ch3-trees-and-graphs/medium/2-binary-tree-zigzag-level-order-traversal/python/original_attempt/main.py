
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS for Level Order Traversal
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()



def main():
    sol = Solution()

    root = [3,9,20,None,None,15,7]

    # Output: [[3],[20,9],[15,7]]
    print(sol.zigzagLevelOrder(root))