class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        root: TreeNode
        rtype: List[int]
        """
        if root is None:
            return

        self.inorderTraversal(root.left)
        print(root.val)

        self.inorderTraversal(root.right)

def main():
    tree = TreeNode(1)
    tree.left = None
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    soln = Solution()
    soln.inorderTraversal(tree)

if __name__ == "__main__":
    main()
