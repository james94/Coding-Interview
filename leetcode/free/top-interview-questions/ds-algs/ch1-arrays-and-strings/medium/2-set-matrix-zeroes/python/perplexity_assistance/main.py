
# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#12

##
# Before Coding:
##
# Data Structures & Algorithms
##
#
# - Matrix Traversal: Row-wise and column-wise iteration to mark zeros.
#
# - In-Place Modification: Use the matrix itself to track rows/columns to be
#   zeroed without extra space
#
# Clarifying Questions:
##
#
# 1. Can we modify the matrix in place?
#   - Yes, the problem requires an in-place solution.
#
# 2. How to handle the first row and column when using them as markers?
#   - Track whether the first row/column initially contains zeros separately.
#
##
# Potential Solutions/After Coding:
##
#
# Time Complexity: O(m+n): Track rows and columns to zero using two arrays
#
# Space Complexity: Constant Space O(1): Use the first row and column as markers, with
#   two variables for the first row/column
#
# Edge Cases:
#   - Matrices where the first row/column contains zeros.
#   - Matrices with all elements as zeros.
##
# While Coding: Explanation of Solution
##
#
# 1. Track First Row/Column:
#   - Check if the first row or column contains zeros initially
#
# 2. Mark Zeros:
#   - For each cell (i, j) where i >= 1 and j >= 1, mark the first element of its row
#   (matrix[i]) and column (matrix[j]) as 0 if the cell is 0
#
# 3. Zero Marked Rows/Columns:
#   - Iterate through the first column (excluding row 0) and zero rows where matrix[i] == 0
#   - Iterate through the first row (excluding column 0) and zero columns where matrix[j] == 0
#
# 4. Handle First Row/Column:
#   - Zero the entire first row/column if they initially contained zeros.
#

def setZeroes(matrix):
    m = len(matrix)
    if m == 0:
        return
    
    n = len(matrix[0])

    # Check if first row/column has zeros
    first_row_zero = any(cell == 0 for cell in matrix[0])
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row/column to mark zeros for the rest of the matrix
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0 # Mark row
                matrix[0][j] = 0 # Mark column
    
    # Zero out marked rows (excluding first row)
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0
    
    # Zero out marked columns (excluding first column)
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    # Zero out first row/column if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

def main():
    # Example 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    setZeroes(matrix1)
    print(f"Example 1 Output: {matrix1}")

    # Example 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    setZeroes(matrix2)
    print(f"Example 2 Output: {matrix2}")

if __name__ == "__main__":
    main()
