from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node once.

Space Complexity: O(h) for the recursion stack (where h is the height of the tree) + O(n) for the
    result list. In the worst case of a skewed tree, this becomes O(n).
"""
def levelOrderTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    def traverse(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        """
        Recursive helper function 'traverse' takes the current node, level, and result list
        """

        # base case is when the node is None, which handles empty trees or leaf nodes
        if not node:
            return
        
        # extend the list if we encounter a new level, demonstrating dynamic data structure manipulation
        if len(result) <= level:
            result.append([])

        # append the current node's value to the appropriate level in the result
        result[level].append(node.val)

        # recursively call the function for left and right children, incrementing the level
        traverse(node.left, level + 1, result)
        traverse(node.right, level + 1, result)

    result = []
    traverse(root, 0, result)
    return result

def main():
    # NBA example: Team hierarchy
    ceo = TreeNode("Adam Silver")
    ceo.left = TreeNode("Mark Tatum")
    ceo.right = TreeNode("Michael Bass")
    ceo.left.left = TreeNode("Byron Spruell")
    ceo.left.right = TreeNode("Amy Brooks")
    ceo.right.left = TreeNode("Dan Rossomondo")
    ceo.right.right = TreeNode("Oris Stuart")

    print("NBA Executive Hierarchy:")
    hierarchy = levelOrderTraversal(ceo)
    for level, executives in enumerate(hierarchy):
        print(f"Level {level}: {', '.join(executives)}")

if __name__ == "__main__":
    main()
