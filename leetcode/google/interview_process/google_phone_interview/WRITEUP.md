# Google Phone Interview (Solution)

## Approach

Follow these steps to approach Google Software Engineer Phone Interview:

1. Clarify requirements and constraints
2. Devise a high-level algorithm
3. Implement the solution in C++20
4. Optimize and analyze complexity
5. Consider edge cases and testing

We'll walk through this process with a common interview question LRU Cache

## Problem: Implement a LRU Cache

Implement a data structure for a Least Recently Used (LRU) cache.

### Step 1: Clarify Requirements

- What is the maximum size of the cache?
- What types are the keys and values?
- What should happen when the cache is full and a new item is added?
- Should the get operation update the item's position in the cache?

Assumptions:

- The cache has a fixed maximum size.
- Keys and values are integers.
- When the cache is full, the least recently used item is evicted.
- Both get and put operations should count as "use" of an item

### Step 2: High-Level Algorithm

1. Use a hash map for O(1) lookup of key-value pairs.
2. Use a doubly linked list to maintain the order of items by recency.
3. For get operations, move the accessed item to the front of the list.
4. For put operations, add new items to the front and remove the least recent if full.

### Step 3: C++20 Implementation

~~~cpp
~~~

### Step 4: Optimization and Complexity Analysis

Time Complexity:

- get: O(1) average case
- put: O(1) average case

Space Complexity:

- O(capacity) for storing up to "capacity" elements

The implementation uses `std::unordered_map` for O(1) average case lookup and `std::list` for O(1) insertion and deletion at both ends. The splice operation in `std::list` is also O(1), making our get and put operations efficient.

### Step 5: Edge Cases and Testing

Edge cases to consider:

1. Accessing a non-existent key
2. Adding an item when the cache is full
3. Updating an existing item
4. Multiple get operations on the same key

Test cases:

~~~cpp
~~~

This approach demonstrates:

1. Clear problem understanding
2. Efficient algorithm design
3. Modern C++20 implementation
4. Complexity analysis
5. Consideration of edge cases and testing

## Resources

- While exploring how to solve this problem, I had assistance from Perplexity AI on how to solve it from a software design and development perspective: https://www.perplexity.ai/search/you-are-a-software-engineer-ai-tbFWfv1hRIKGgsuupoIAWA
