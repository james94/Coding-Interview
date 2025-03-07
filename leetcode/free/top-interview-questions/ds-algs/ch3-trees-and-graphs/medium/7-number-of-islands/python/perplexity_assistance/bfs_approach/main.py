from collections import deque
from typing import List

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#9

##
# Before Coding:
##
# Data Structures & Algorithms
#
# 2D Grids: problem involves a 2D grid representing a map of 1's (land) and 0's (water)
#
# Breadth-First Search (BFS): BFS explores all neighbors level by level, making it suitable
# for finding connected components in a grid.
#
# Queue: A queue is used to mange the BFS traversal.
#
##
# Clarifying Questions:
##
#
# 1. How are islands defined? Islands are formed by connected adjacent cells horizontally or
#       vertically.
#
# 2. Are diagonally connected cells considered part of the same island?
#      - No, only horizontal and vertical connections are considered.
#
# 3. What should the function return when the grid is empty?
#      - Return 0 as there are no islands.
#
# Potential Solutions:
#
# DFS Solution: Use DFS to mark all connected lands as visited when an island is found
#
# BFS Solution: Use BFS to explore islands level by level, marking visited lands
#
##
# Explanation of BFS Approach:
##
#
# 1. Initialization:
#   - Use a deque to implement BFS queue
#   - Start BFS whenever an unvisted land cell ("1") is found
# 2. Marking Visited Cells:
#   - As we explore each cell during BFS, mark it as water ("0") to avoid revisiting it
# 3. Exploring Neighbors:
#   - For each cell (r, c), add its valid neighbors (up, down, left, right) to the queue
#       if they are land ("1")
# 4. Counting Islands:
#   - Increment the island_count every time a new BFS is initiated from an unvisited land cell.
#
##
# Potential Improvements:
##
#
# Time Complexity: BFS solution has a time complexity of O(m*n), where "m" and "n" are
# the dimensions of the grid, m is the number of rows and n is the number of columns.
# Each cell is visited once.
#
# Space Complexity: O(min(m*n)) due to the maximum size of the queue in BFS
#
# Edge Cases:
#   - Empty grid (grid=[]): Return island_count = 0
#   - Grid with no land (grid=[["000"]]): Return island_count = .
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()

                # Explore all four directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    # If the neighbor is within bounds and is land ("1")
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0" # Mark as visited
                        queue.append((nr, nc))

        # Iterate through the grid
        for row in range(rows):
            for col in range(cols):
                # Found an unvisited land cell
                if grid[row][col] == "1":
                    bfs(row, col)
                    island_count += 1

        return island_count

def main():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    # grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]

    soln = Solution()
    print(soln.numIslands(grid))

if __name__ == "__main__":
    main()

