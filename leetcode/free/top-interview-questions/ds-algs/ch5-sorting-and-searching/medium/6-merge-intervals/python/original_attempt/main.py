# Maybe about 20 mins
class Solution:
    def merge(self, inervals: List[List[int]]) -> List[List[int]]:
        result = []

        num_rows, num_cols = len(intervals), len(intervals[0])
        start_i = 0
        end_i = 1

        row_i = 0

        prev_start = intervals[row_i][start_i]
        prev_end = intervals[row_i][end_i]

        for row_i in range(1, len(intervals)):
            start_elm = intervals[row_i][start_i]
            end_elm = intervals[row_i][end_i]

            if start_elm <= prev_end:
                print("Overlap")
                result.append([prev_start, end_elm])
            else:
                result.append([start_elm, end_elm])

            prev_start = start_elm
            prev_end = end_elm


