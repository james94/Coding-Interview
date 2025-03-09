# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#23


##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Sorting: To arrange intervals in order of start times.
# - Array/List: To store and manipulate
# - Linear Traversal: To merge overlapping intervals
#
##
# Clarifying Questions:
##
#
# 1. Can the intervals be in any order in the input?
#   - Yes, we should assume they can be in any order.
#
# 2. How should we handle intervals that touch but don't overlap (ex: and)?
#   - Based on the example, we should merge such intervals
#
# 3. Are the start and end times inclusive or exclusive?
#   - We can assume they are inclusive based on the examples.
#
# Potential Solutions:
#
# 1. Sort and Merge: Sort intervals by start time, then merge in a single pass
#
# 2. Line Sweep Algorithm: Track start and end events separately
#
# This is primarily a Sorting problem, with elements of array manipulation.
#
##
# Explanation of Sort and Merge Approach:
##
#
# 1. Sort the intervals based on start times.
#
# 2. Iterate through sorted intervals:
#   - If merged is empty or current interval doesn't overlap, add it to merged.
#   - If there's no overlap, extend the previous interval's end time if necessary
#
##
# After Coding:
##
#
# Time Complexity: O(n * log*n) due to sorting, where n is the number of intervals
#
# Space Complexity: O(n) to store the output. Sorting may require O(n) space depending on the implementation
#
# Potential Improvements:
#
# 1. In-Place Sorting: If allowed, sort the input array in-place to save space.
#
# 2. Custom Sort: Implement a custom sorting algorithm if the range of start times is small and known.
#
# Edge Cases:
#
# - Single Interval
# - All intervals overlapping
# - No overlapping intervals
# - Intervals that touch but don't overlap (ex: and)

##
# Summary
##
#
# This solution efficiently merges overlapping intervals by first sorting them and then
#   merging in a single pass, handling various cases including touching intervals and complete overlaps.
#


from typing import List

# We use Sort and Merge Approach
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []

        for interval in intervals:
            # Descriptive names for current interval
            current_start, current_end = interval

            # If merged is empty or current interval doesn't overlap with the last merged interval
            if not merged or merged[-1][1] < current_start:
                # Add the current interval as a new non-overlapping interval
                merged.append(interval)
            else:
                # Merge with the last interval in the merged list
                    # Descriptive names for last merged interval
                last_merged_start, last_merged_end = merged[-1]
                # Update the end of the last merged interval
                merged[-1][1] = max(last_merged_end, current_end)

        return merged


def main():
    sol = Solution()

    intervals1 = [[1,3],[2,6],[8,10],[15,18]]

    print(sol.merge(intervals1))

    intervals2 = [[1,4],[4,5]]

    print(sol.merge(intervals2))

if __name__ == "__main__":
    main()