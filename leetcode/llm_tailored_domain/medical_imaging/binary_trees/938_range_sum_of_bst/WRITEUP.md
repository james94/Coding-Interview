# 938. Range Sum of BST (Medical Imaging) Solution

## Software Design

For this medical imaging analysis problem, we'll use a binary tree represent the hierarchical segmentation of brain regions.
We'll implement a depth-first search (DFS) traversal of the binary tree to efficiently sum the intensities within the given range.
The solution will use recursion for simplicity and readability.

## Time Complexity

**Time Complexity:** O(N) where N is the number of nodes in the binary tree. In the worst case, we might need to visit all nodes.

## Space Complexity

**Space Complexity:** O(H) where H is the height of the tree. This space is used by the recursive call stack. In the worst
case (skewed tree), it could be O(N).

## C++ Implementation

Refer to [cpp/main.cpp](./cpp/main.cpp) for C++ implementation.

## Software Methodology

This C++ implementation addresses the requirements:

1\. Efficient traversal: Uses a DFS approach, pruning unnecessary branches

2\. Edge cases: Handles null nodes and out-of-range values.

3\. Time/Space Complexity: addressed above

4\. Parallelization potential: The current implementation is sequential, but could be parallelized by processing left and right subtrees concurrently for large datasets.

5\. Error handling: Uses exception handling for input validation.

6\. Unit testing strategy: Test cases should include:

- Normal case (as given in the example)
- Edge cases (empty tree, single node tree)
- All nodes outside range
- All nodes inside range
- Tree with negative intensities (if allowed)
- Various tree shapes (balanced, skewed left/right)

## C++ Python Bindings Methodology

1\. We defined a `PyTreeNode` class that mirrors our C++ `TreeNode` structure but is more Python friendly

2\. We created a `py_analyzeBrainRegions` function that converts the Python tree sgtructure to our C++ structure,
    calls our C++ `analyzeBrainRegions` function and returns the result.

3\. We used pybind11 to create a Python module called `brain_region_analysis` with a `TreeNode` class and an `analyze_brain_regions` function.

## C++ Solution

~~~bash
cd cpp

mkdir build

cmake ..
make

./brain_region_range_sum_bst

cd ..
~~~

## PyBind Solution

~~~bash
cd py

mkdir build

cmake ..
make

python3 brain_region_analysis.py

cd ..
~~~

- NOTE: might need to add docker support for easier reproducibility of building and running programs

## Resource

Perplexity AI updated wording of leetcode question tailoring for this medical imaging problem, also includes the solution and other important links: https://www.perplexity.ai/search/you-are-a-software-infrastruct-AfXf_DZdRAKTJGnQ7rnuwA

## Citations

- [1] https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2024.1349111/full
- [2] https://simtk.org/pastopportunities.php
- [3] https://www.nicolaromano.net/data-thoughts/binary-trees-classification/
- [4] https://news.ycombinator.com/item?id=41709299
- [5] https://link.springer.com/article/10.1007/s11042-022-14305-w
- [6] https://cooper.edu/engineering/curriculum/courses
- [7] https://pmc.ncbi.nlm.nih.gov/articles/PMC10662291/
- [8] https://www.mdpi.com/2073-8994/15/12/2213
