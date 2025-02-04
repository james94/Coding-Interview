from typing import List

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#4

##
# Before Coding:
##
# Data Structures & Algorithms
#
# 2D Grids: problem involves a 2D grid representing a map of 1's (land) and 0's (water)
#
# Depth-First Search (DFS): This algorithm is suitable for traversing connected lands
# (islands) in the grid
#
# Breadth-First Search (BFS): Alternatively, BFS can be used to explore islands level by level
#
# Potential Solutions:
#
# DFS Solution: Use DFS to mark all connected lands as visited when an island is found
# 
# BFS Solution: Use BFS to explore islands level by level, marking visited lands
#
##
# Explanation:
##
#
# DFS Approach: Iterate through the grid. When a '1' (land) is found, perform DFS to mark all
# connected lands as visited '0'
#
# Island Counting: Increment the island count each time a new island is discovered
#
#
##
# Potential Improvements:
##
#
# Time Complexity: DFS solution has a time complexity of O(m*n), where "m" and "n" are
# the dimensions of the grid
#
# Space Complexity: O(m*n) in the worst case due to the recursive call stack
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(row: int, col: int) -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
                return
            
            grid[row][col] = "0" # Mark as visited

            dfs(row - 1, col) # Up
            dfs(row + 1, col) # Down
            dfs(row, col - 1) # Left
            dfs(row, col + 1) # Right

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    island_count += 1

        return island_count

def main():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    soln = Solution()
    print(soln.numIslands(grid))

if __name__ == "__main__":
    main()

