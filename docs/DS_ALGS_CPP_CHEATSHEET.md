# DS & Algs C++20 Cheatsheet

Perplexity AI reference for **C++20 APIs** related to Data Structures & Algorithms with a touch of Deep Learning cheatsheet: https://www.perplexity.ai/search/you-are-a-software-deep-learni-hvH6ASHhTyu0v74jPTECaw

Perplexity AI reference for C++20 APIs related to Data Structures & Algorithms with some emphasis on simulations cheatsheet: https://www.perplexity.ai/search/you-are-a-software-infrastruct-47SsZf5jSyqxSgdUnUHSQQ

- C++ API Reference: https://en.cppreference.com/w/

## Data Structures

### Arrays (2D/3D)

C++20 introduces `std::span` for safer array views:

~~~cpp
#include <span>
std::array<int, 3> arr = {1, 2, 3};
std::span<int> view = arr;
~~~

For multidimensional arrays, consider using `std::vector` with custom indexing:

~~~cpp
std::vector<int> matrix(rows * cols);
auto at = [&](int i, int j) -> int& { return matrix[i * cols + j]; };
~~~

**Design & Development:**

- Use `std::array` for fixed-size arrays or `std::vector` for dynamic arrays
- For 2D/3D arrays, consider using nested containers or a single container with index mapping

**C++20 Features:**

- Use `std::span` for non-owning views of contiguous sequences
- Utilize `std::ranges` for more expressive array operations

**Complexity:**

- Access: **O(1)**
- Insertion/Deletion at end: **O(1)** amortized
- Insertion/Deletion at arbitrary position: **O(n)**

Example:

~~~cpp
std::vector<std::vector<int>> grid2D(rows, std::vector<int>(cols));
std::vector<int> grid3D(x * y * z);
auto element = grid3D[x + y * width + z * width * height];
~~~

### Linked Lists

Use `std::forward_list` for singly-linked lists and `std::list` for doubly-linked lists:

~~~cpp
#include <forward_list>
#include <list>

std::forward_list<int> sll = {1, 2, 3};
std::list<int> dll = {1, 2, 3};
~~~

**Design & Development:**

- Use `std::forward_list` for singly-linked lists or `std::list` for doubly-linked lists
- For custom implementations, use smart pointers like `std::unique_ptr` for memory management

**C++20 Features:**

- Utilize concepts to constrain template parameters for list operations

**Complexity:**

- Access: **O(n)**
- Insertion/Deletion at beginning: **O(1)**
- Insertion/Deletion at end: **O(1)** for doubly-linked, **O(n)** for singly-linked

Reverse Linked List:

~~~cpp
template<std::forward_iterator It>
void reverse_list(It& head) {
    It prev = nullptr, current = head, next = nullptr;
    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}
~~~

### Hash Tables

Utilize `std::unordered_map` and `std::unordered_set`:

~~~cpp
#include <unordered_map>
#include <unordered_set>

std::unordered_map<std::string, int> map;
std::unordered_set<int> set;
~~~



**Design & Development:**

- Use `std::unordered_map` or `std::unordered_set` for hash-based containers
- Consider custom hash functions for complex keys

**C++20 Features:**

- Use `contains()` member function for efficient key presence checks

**Complexity:**

- Average case: **O(1)** for insertion, deletion, and search
- Worst case: **O(n)** when hash collisions are frequent

Example:

~~~cpp
std::unordered_map<std::string, int> hash_table;
if (hash_table.contains("key")) {
    // Key exists
}
~~~

### Stacks and Queues

Use `std::stack` and `std::queue`:

~~~cpp
#include <stack>
#include <queue>

std::stack<int> stack;
std::queue<int> queue;
~~~


**Design & Development:**

- Use `std::stack` for LIFO operations and `std::queue` for FIFO operations
- These are container adaptors, typically implemented using `std::deque`

**Complexity:**

- Push/Pop: **O(1)**
- Top/Front access: **O(1)**

### Heaps

Implement with `std::priority_queue`:

~~~cpp
#include <queue>

std::priority_queue<int> max_heap;
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
~~~


**Design & Development:**

- Use `std::priority_queue` for heap operations
- For custom heaps, implement the heap property manually

**C++20 Features:**

- Use `std::ranges` for more expressive heap operations

**Complexity:**

- Insertion: **O(log n)**
- Extraction of max/min element: **O(log n)**
- Peek max/min: **O(1)**


## Trees

Implement custom tree structures:

~~~cpp
struct TreeNode {
    int val;
    std::vector<TreeNode*> children;
};
~~~


**Design & Development:**

- Implement custom node structure for binary trees
- Use recursive or iterative approaches for tree operations

**Complexity:**

- Balanced tree operations: **O(log n)** average case
- Unbalanced tree: **O(n)** worst case

### Tree Traversal

Implement custom traversal functions:

~~~cpp
void inorderTraversal(TreeNode* root) {
    if (root) {
        inorderTraversal(root->left);
        std::cout << root->val << " ";
        inorderTraversal(root->right);
    }
}
~~~


## Algorithms

### Sorting

Use `std::sort` with C++20 ranges:

~~~cpp
#include <algorithm>
#include <ranges>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
std::ranges::sort(v);
~~~


**Design & Development:**

- Use `std::sort` for general-purpose sorting
- For specific needs, implement custom sorting algorithms

**C++20 Features:**

- Use `std::ranges::sort` for more flexible sorting operations

**Complexity:**

- Quick Sort, Merge Sort: **O(n log n)** average case
- Bubble Sort, Insertion Sort: **O(n^2)**


### Searching

Utilize `std::ranges::find` and `std::ranges::binary_search`:

~~~cpp
auto it = std::ranges::find(v, 4);
bool found = std::ranges::binary_search(v, 4);
~~~


**Design & Development:**

- Use `std::binary_search` for sorted containers
- Implement custom search algorithms for specific data structures

**C++20 Features:**

- Use `std::ranges::binary_search` for more flexible binary search

**Complexity:**

- Binary Search: **O(log n)**
- Linear Search: **O(n)**

### Graph Traversal

Implement BFS and DFS using `std::queue` or `std::stack`:

~~~cpp
void bfs(Graph& g, int start) {
    std::queue<int> q;
    std::vector<bool> visited(g.size(), false);
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : g[v]) {
            if (!visited[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
    }
}
~~~

**Design & Development:**

- Implement graphs using adjacency lists (vector of vectors) or adjacency matrices
- Use `std::unordered_map` for efficient vertex lookup in sparse graphs

**Graph Traversal:**

- Depth-First Search (DFS): Use recursion or stack
- Breadth-First Search (BFS): Use queue

**Complexity:**

- DFS/BFS: **O(V + E)** for adjacency list, **O(V^2)** for adjacency matrix
- Where **V** is the number of vertices and **E** is the number of edges

Example:

~~~cpp
std::vector<std::vector<int>> graph(num_vertices);
std::vector<bool> visited(num_vertices, false);

void dfs(int v) {
    visited[v] = true;
    for (int u : graph[v]) {
        if (!visited[u]) dfs(u);
    }
}
~~~

## General C++20 Features for Data Structures & Algorithms

- **Concepts**: Use to constrain template parameters and improve error messages
- **Ranges**: Utilize for more expressive and composable algorithms
- **Coroutines**: Consider for implementing lazy evaluation in complex algorithms
- **Modules**: Use to improve compilation times and encapsulation
- **constexpr**: Leverage for compile-time computation of algorithms when possible

Remember to profile your code and choose data structures based on the specific requirements of your simulation. The choice between different implementations can significantly impact performance in real-life simulations[1].


## Citations:

[1] https://www.pearson.com/en-us/pearsonplus/p/9780138122805
[2] https://drops.dagstuhl.de/storage/00lipics/lipics-vol222-ecoop2022/LIPIcs.ECOOP.2022.31/LIPIcs.ECOOP.2022.31.pdf
[3] https://www.geeksforgeeks.org/features-of-c-20/
[4] https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-32018.pdf
[5] https://www.youtube.com/watch?v=jCnBFjkVuN0
[6] https://www.pearson.com/en-us/subject-catalog/p/secure-data-structures-and-algorithms-with-c-walls-and-mirrors/P200000010315/9780138122805
[7] https://stackoverflow.com/questions/40642021/c-fastest-data-structure-for-multiple-searches
[8] https://www.reddit.com/r/C_Programming/comments/11s50vf/so_whats_the_best_data_structures_and_algorithms/
