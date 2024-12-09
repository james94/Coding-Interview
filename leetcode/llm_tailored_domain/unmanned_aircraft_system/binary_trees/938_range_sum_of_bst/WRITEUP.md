# 938. Range Sum of BST (Unmanned Aircraft Systems) Solution

## Software Design Perspective

1\. Define a TreeNode structure to represent each node in the Digital Elevation Model (DEM) binary search tree.

2\. Implement a function to calculate the sum of elevation values within the given range.

3\. Use recursive traversal of the binary search tree to efficiently find and sum the relevant elevation values.

## Time Complexity

- O(N) where N is the number of nodes in the tree. In the worst case, we might need to visit all nodes.

## Space Complexity

- O(H) where H is the height of the tree. This is due to the recursive call stack. In the worst case (skewed
tree), it could be O(N), but for a balanced BST, it would be O(logN)
