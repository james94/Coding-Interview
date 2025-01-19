# Recursive Binary Tree Level Order Traversal (Solution)

## Before Coding

### Clarifying questions:

1. Is the complex data structure specifically a binary tree, or could it be
a more general tree or graph?

2. Should we return the traversal as a list of lists, where each inner list
represents a level?

3. Do we need to handle empty trees or null inputs?

4. Is there a specific order we should follow within each level (ex: left to right)?

### Potential solutions:

1. Recursive approach using a helper function to keep track of levels

2. Iterative approach using a queue (BFS)

3. Recursive approach using DFS and sorting by level

## Recursive Binary Tree Level Order Traversal Implementation

We'll proceed with the **recursive approach** using a **helper function**, as it's
a good balance of simplicity and efficiency.

- [main.py](./python/main.py)

## While Coding

### 1. **Data Structures and Algorithms**:

- We use a list of lists to store the level order traversal
- The algorithm is a depth-first search (DFS) with level tracking

### 2. **Big-O Notation**:

- Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node once.

- Space Complexity: O(h) for the recursion stack (where h is the height of the tree) + O(n) for the
    result list. In the worst case of a skewed tree, this becomes O(n).

## After Coding

### Recursive Binary Tree Level Order Traversal: Potential Improvements

1. We could add error handling for invalid inputs, demonstrating attention to edge cases.

2. For very large trees, we might want to consider an iterative solution to avoid stack overflow, showing awareness
of scalability issues.

3. We could add type hints for better code readability and maintainability, which is important for
collaborative develpoment.

4. For a more general tree structure, we could modify the TreeNode class to have a list
of children instead of just left and right

5. To make it more relevant to the NBA, we could extend the TreeNode class to include more basketball-specific
data and implement additional methods for data analysis.

This solution effectively traverses the tree level by level, which meets the requirements of the problem.
The NBA example demonstrates how this algorithm can be applied to represent organizational hierarchies
or other tree-like structures in sports management.

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-K5Wy_yk1Rz6B3dukkK2y7w
