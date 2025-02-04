from typing import List

class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        for row in grid:
            for col in grid[row]:

def main():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

if __name__ == "__main__":
    main()
