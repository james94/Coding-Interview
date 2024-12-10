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

## C++ Implementation

Refer to [cpp/main.cpp](./cpp/main.cpp) for C++ implementation.

## Run C++ Solution

~~~bash
cd cpp

mkdir build

cmake ..
make

./terrain_navigation_range_sum_bst

cd ..
~~~

## Run PyBind Solution

~~~bash
cd py

mkdir build

cmake ..
make

python3 terrain_navigation_dem_tracker.py

cd ..
~~~

## Handling Additional Requirements

### Scalability

For larger DEMs and frequent queries, we could implement caching mechanisms to store results of common results of common elevation ranges.
We could also consider using a more balanced tree like an AVL tree or Red-Black tree to ensure O(logN) time complexity for queries.

### Integration Into a Real-Time UAS Navigation System

- This function could be part of a larger Terrain Following module
- It could be called periodically or triggered by changes in the UAS's position or planned path.
- The results could be used to adjust the UAS's altitude or trajectory to maintain safe clearance from terrain

### Handling Errors & Edge Cases In Production

- Implement input validation to ensure low <= high and both are within valid elevation ranges.
- Use exception handling to gracefully manage unexpected scenarios (e.g. corrupted tree structure).
- Implement logging for debugging and monitoring system performance
- Consider thread-safety if the function might be called concurrently from multiple parts of the system.
- Implement unit tests to cover various scenarios, including edge cases
