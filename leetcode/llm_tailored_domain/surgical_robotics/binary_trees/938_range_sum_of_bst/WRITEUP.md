# 938. Range Sum of BST (Surgical Robotics) Solution

## Software Design Perspective

1\. We'll use a Binary Search Tree (BST) to represent the surgical instruments' positions.

2\. We'll implement a recursive fucntion to traverse the BST and sum the values within the given range.

3\. We'll use a class to encapsulate the BST node structure and the main function.

## Time Complexity

- O(N) where N is the number of nodes in the tree. In the worst case, we might need to visit all nodes.

## Space Complexity

- O(H) where H is the height of the tree. This is due to the recursive call stack. In the worst case (skewed
tree), it could be O(N), but for a balanced BST, it would be O(logN)

## C++ Implementation

Refer to [cpp/main.cpp](./cpp/main.cpp) for C++ implementation.

## C++ Methodology

1\. We defined a `SurgicalInstrumentTracker` class that encapsulates the BST and related operations

2\. The `TreeNode` struct represents each node in the BST

3\. We implemented `insert` and `sumInRange` methods as the public interface.

4\. The `sumInRangeRec` method recursively traverses the BST and sums the values within the given range.

5\. We used a mutex (`treeMutex`) to ensure thread safety when accessing or modifying the tree.

## Scaling for Larger Datasets & Optimizations

1\. The current implementation scales well for balanced BSTs (O(logN) average case for insertions and range queries)

2\. For very large datasets, we could consider using a self-balancing BST (like Red-Black Tree) to ensure
O(logN) worst-case performance.

3\. We could implement a caching mechanism for frequently queried ranges to improve performance.

## Handling Real-Time Updates

1\. The current implementation already supports real-time insertions thorugh the `insert` method.

2\. To handle updates of existing positions, we could add an `update` method that first removes the old position and then inserts the new one.

3\. For frequent updates, we might consider using a more specialized data structure like a segment tree or a Fenwick tree, which can handle range queries and updates more efficiently.
