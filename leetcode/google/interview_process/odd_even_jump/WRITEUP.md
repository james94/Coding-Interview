# Odd Even Jump (Solution)

We will break down our solution.

## Data Structures

- We use two boolean vectors `odd` and `even` for dynamic programming to store whether we can reach the end from each index using odd and even jumps.
- We use a `std::map<int, int>` to store value-to-index mappings finding the next larger or smaller element.

## Algorithm

- We iterate through the array from right to left.
- **Next Jump Calaculation:** For each index, we determine where an odd jump and an even jump would lead.
- **Reachability Computation:** We use the results of previous computations to determine if we can reach the end from the current index.
- **Result Aggregation:** Count the number of good starting indices

### Preprocessing

- Sort the array indices based on their values to efficiently find next larger/smaller elements.
- Use a monotonic stack to precompute next jump indices for both odd and even jumps.

## Time Complexity: O(n log n)

- The main loop runs `n` times.
- Each map operation (lower_bound, upper_bound, insertion) takes `O(log n)

## Time Complexity: O(n)

- We use two boolean vectors of size `n` and a map that can store up to `n` elements.

## Software Infrastructure Design

- This solution is designed to be efficient and scalable
- It uses C++20 features and standard library containers for better performance and readability.
- The code is encapsulated in a class, making it easy to integrate into larger systems.

## Software Infrastructure Development

- The use of `std::map` allows for efficient lookups and insertions
- We use iterators and C++ standard library functions for clean and efficient code.
- The solution respects the given constraints and handles edge cases (e.g., arrays of size 0 or 1)

## Software Methodology (Dynamic Programming)

- Initialize `odd` and `even` vectors with `false`, except for the last index.
    - Initialize the last index as reachable for both odd and even jumps.
- Iterate from right to left (updating reachability for each index):
    - For odd jumps: check if the next larger element is reachable by an even jump.
        - Find the next larger or equal value (for odd jumps) using `lower_bound`.
    - For even jumps: check if the next smaller element is reachable by an odd jump.
        - Find the next smaller value (for even jumps) using `upper_bound`.
    - Update `odd[i]` and `even[i]` based on the results of these jumps.
    - If `odd[i]` is true, increment the count of good indices.
    - Add the current value-index pair to the map

## Implementation

### C++ Approach

Check out our [Odd Even Jump: C++ solution approach](./cpp/main.cpp)

## Resources

- While exploring how to solve this problem, I had assistance from Perplexity AI on how to solve it from a software design and development perspective: https://www.perplexity.ai/search/you-are-a-software-engineer-ai-i0r5eXGZRyGpsom6YMRiCQ
