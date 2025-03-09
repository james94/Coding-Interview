# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#18

##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Matrix Traversal: Efficiently navigate through rows and columns
# - Search Optimization: Leverage sorted properties to eliminate rows/columns quickly
#
##
# Clarifying Questions:
##
#
# 1. Are rows and columns fully sorted?
#   - Yes: Rows are sorted left to right, columns are sorted top to bottom
#
# 2. Can we exploit these sorted properties to optimize the search?
#   - Yes: Start from the top-right or bottom-left corner to make directional decisions
#
# Potential Solutions:
#
# 1. Stepwise Search (Optimal):
#   - Start at the top-right corner
#   - Move left if the current value is greater than the target
#   - Move down if the current value is smaller than the target
#
# Time Complexity: O(m+n)
#
# Space Complexity: O(1)
#
# 2. Binary Search Per Row:
#   - For each row, perform a binary search
#
# Time Complexity: O(m * log * n)
#
# Space Complexity: O(1)
#
##
# Explanation of Stepwise Search Approach:
##
#
# 1. Initialization:
#   - Start at the top-right corner (row=0, col=n-1)
#
# 2. Traversal:
#   - If the current value equals the target, return True
#   - If the current value is less than target, move down (next row)
#   - If the current value is greater than the target, move left (previous column)
#
# 3. Termination:
#   - Exit when row or col goes out of bounds, returning False
#
#
##
# After Coding:
##
#
# Time Complexity: O(m+n) - At worst, traverse one full row and column
#
# Space Complexity: O(1) - No extra space used
#
##
# Potential Improvements:
##
#
# 1. Binary Search Hybrid:
#   - Combine stepwise movement with binary search for larger matrices.
#
# 2. Divide and Conquer:
#   - Recursively divide the matrix into quadrants, but this complicates implementation
#       without clear benefits for this problem
#
# 3. Parallelization:
#   - For very large matrices, split the search across threads (through overhead might negate benefits)
#
##
# Edge Cases:
##
#
# - Single-cell matrix ( [], target = 5 -> True)
# - Target smaller than all elements -> exit quickly
# - Target larger than all elements -> exit quickly

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1 # Start from top-right corner

        while row < m and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True
            elif current < target:
                row += 1 # Move down to larger values
            else:
                col -= 1 # Move left to smaller values
        
        return False

def main():
    sol = Solution()

    matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target1 = 5

    print(sol.searchMatrix(matrix1, target1)) # Output: True
    
    target2 = 20

    print(sol.searchMatrix(matrix1, target2)) # Output: False

    matrix2 = [[5]]

    print(sol.searchMatrix(matrix2, target1)) # Output: True
    print(sol.searchMatrix(matrix2, 3)) # Output: False

if __name__ == "__main__":
    main()
