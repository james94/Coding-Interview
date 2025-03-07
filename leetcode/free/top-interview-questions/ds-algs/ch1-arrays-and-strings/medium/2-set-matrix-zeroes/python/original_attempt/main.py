

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
            Modify the matrix in-place
        """
        # This index holds element that is 0
        target_index = (-1, -1)
        for row in len(matrix):
            for col in len(matrix[row]):
                if matrix[row][col] == 0:
                    target_index = (row, col)
        # if row contains same number as target, then zero that cell
        # if col contains same number as target, then zero that cell
        # thus we have zeroed entire row and column with respect to our target that is 0

def main():
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]

    Solution soln
    soln.setZeroes(matrix1)

    print("Set Zeros In-Place - Matrix1:")
    print(matrix1)
