# 1331. Rank Transform of an Array  (Medical Imaging) Solution

## Software Design

To solve the MRI Signal Intensity Ranking problem, we'll use a combination of hash tables and sorting. The approach will be:

1. Create a hash table to store unique intensities and their sorted order.

2. Sort the unique intensities

3. Assign ranks to the sorted intensities

4. Use the hash table to map original intensities to their ranks.

This design allows for efficient ranking while handling duplicate intensities correctly.

## Time Complexity

**Time Complexity:** O(n log n), where n is the number of voxels

- Sorting unique intensities: O(k log k), where k is the number of unique intensities (k <= n)
- Creating the hash table and mapping ranks: O(n)

## Space Complexity

**Space Complexity:** O(n)

- Hash table for unique intensities: O(k)
- Vector sorted unique intensities: O(k)
- Output vector: O(n)

## C++ Implementation

Refer to [cpp/main.cpp](./cpp/main.cpp) for C++ implementation.

## Software Methodology

- Our implementation uses the `MRISignalRanking` class to encapsulate the ranking functionality.
- The `rank_transform` method handles the core logic of ranking the voxel intensities.
- The `main` function demonstrates the usage with the provided test cases.

## C++ Python Bindings Methodology

## Run C++ Solution

~~~bash
cd cpp

mkdir build

cd build

cmake ..
make -j $(nproc)

./mri_rank_transform_array

cd ../../
~~~

<!-- ## Run PyBind Solution

~~~bash
cd py

mkdir build

cmake ..
make

python3 brain_region_analysis.py

cd ..
~~~ -->

<!-- - NOTE: might need to add docker support for easier reproducibility of building and running programs -->

## Resource

Perplexity AI updated wording of leetcode question tailoring for this medical imaging problem, also includes the solution and other important links: https://www.perplexity.ai/search/you-are-a-software-infrastruct-1T73.QI7TrGVBVjp0uB9dg

## Citations

- [1] https://developers.redhat.com/blog/2017/02/27/towards-faster-ruby-hash-tables
- [2] https://simtk.org/pastopportunities.php
- [3] https://www.reddit.com/r/C_Programming/comments/1832ed5/hash_tables_when_do_i_implement_and_use_them/
- [4] https://catalogs.umn.edu/sites/catalogs.umn.edu/files/2022-12/Twin%20Cities%20Graduate%20Courses%2022-24.pdf
- [5] https://pmc.ncbi.nlm.nih.gov/articles/PMC4967038/
- [6] https://cooper.edu/engineering/curriculum/courses
- [7] https://www.mrisoftware.com/resources/how-to-plan-for-your-successful-mri-implementation/
- [8] https://www.glassdoor.com/Interview/software-infrastructure-engineer-interview-questions-SRCH_KO0,32_SDMC.htm
- [9] https://www.linkedin.com/posts/liv-erickson_i-used-to-think-that-i-didnt-like-to-code-activity-7257491813882630145-8ClQ
