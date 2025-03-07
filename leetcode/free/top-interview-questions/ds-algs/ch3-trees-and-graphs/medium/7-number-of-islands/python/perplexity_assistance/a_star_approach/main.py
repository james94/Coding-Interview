import torch
from heapq import heappush, heappop
from typing import List

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#10

#
# To solve the Number of Islands problem using A* Search Algorithm with PyTorch, we need to adapt
#   A* to identify connected components in the grid. A* is typically used for pathfinding,
#   but we can modify it to explore all reachable cells in an island by treating the grid as a graph.
#

##
# Before Coding:
##
# Data Structures & Algorithms
#
# 2D Grids: problem involves a 2D grid representing a map of 1's (land) and 0's (water)
#
# A* Search Algorithm: A heuristic-based search algorithm that uses a priority queue
#   to explore nodes. It evaluates nodes based on "f(n) = g(n) + h(n)" where:
#
#   - g(n): is the cost to reach the current node
#   - h(n): is the heuristic estimating the cost to reach the goal
#
# Heuristic for Islands: Since we are identifying connected components (not finding a
#   specific goal), we can use a simple heuristic like the Manhattan distance from the
#   current cell to the furthest edge of the grid.
#
##
# Clarifying Questions:
##
#
# 1. How are islands defined? Islands are formed by connected adjacent cells horizontally or
#       vertically. An island is group of connected 1's (land) surrounded by 0's (water).
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
#   - A* Search Algorithm: Treat each land cell as a node and a priority queue to explore neighbors.
#
##
# Explanation of BFS Approach:
##
#
# 1. Initialization:
#   - Use PyTorch's torch.zeros tensor to track visited cells efficiently
#   - Define a "Manhattan distance heuristic" for prioritizing exploration

# 2. A* Search:
#   - Use a priority queue (heapq) to explore neighbors based on their heuristic values.
#   - Mark cells as visited when dequeued from priority queue
#   - Push unvisited land neighbors into the priority queue
#
# 4. Counting Islands:
#   - For each unvisited land cell ("1"), start an A* search and increment the island_count
#
##
# Potential Improvements:
##
#
# Time Complexity: O(m*n) because each cell is visited once during exploration
#
# Space Complexity: O(m*n) due to the visited tensor and the priority queue
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
        visited = torch.zeros((rows, cols), dtype=torch.bool) # Use PyTorch for visited tracking
        island_count = 0

        # Heuristic function (Manhattan distance)
        def heuristic(r, c):
            return max(rows - r - 1, cols - c -1)

        # A* Search for exploring an island
        def a_star(r, c):
            pq = [] # Priority queue for A*
            heappush(pq, (0 + heuristic(r, c), r, c)) # Push (f(n), row, col)

            while pq:
                _, row, col = heappop(pq)

                # Skip if already visited
                if visited[row, col]:
                    continue

                visited[row, col] = True

                # Explore neighbors (up, down, left, right)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr, nc] and grid[nr][nc] == "1":
                        heappush(pq, (heuristic(nr, nc), nr, nc))

        # Main loop to count islands
        for row in range(rows):
            for col in range(cols):
                # Found an unvisited land cell
                if grid[row][col] == "1" and not visited[row, col]:
                    a_star(row, col)
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

