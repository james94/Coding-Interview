from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_dict = {}
        found_target = False

        for i_idx, row in enumerate(matrix):
            for j_idx, value in enumerate(row):
                row_dict[value] = j_idx

            print(f"row_dict = {row_dict}")

            if target in row_dict:
                found_target = True
                return found_target

        return found_target


def main():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5

    sol = Solution()
    print("Search Matrix for Target = ", target)
    print(sol.searchMatrix(matrix, target))


if __name__ == "__main__":
    main()
