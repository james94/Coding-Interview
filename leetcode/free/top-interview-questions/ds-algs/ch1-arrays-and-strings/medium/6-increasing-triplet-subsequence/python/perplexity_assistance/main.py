# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#28
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Greedy Algorithm: Track the smallest possible values for the first and second elements of a potential triplet
#
# - Linear Traversal: Process each element once to update the first and second values
#
# Clarifying Questions:
#
# 1. Can the triplet elements be non-consecutive?
#   - Yes, as long as they appear in order (i < j < k)
#
# 2. What if there are multiple valid triplets?
#   - The algorithm needs to return true if at least one exists
#
# Potential Solutions:
#
# 1. Brute Force: Check all possible triplets (O(n^3) time)
#
# 2. Dynamic Programming: Track the longest increasing subsequence (O(n^2) time)
#
# 3. Greedy Approach: Track the smallest first and second elements to find a valid third element (O(n) time, O(1) space)
# 
#
##
# After Coding
##
#
#   - Time Complexity: O(n)
#       - Each element is processed exactly once.
#   - Space Complexity: O(1)
#       - Only two variables (first and second) are used.
#   - Edge Cases:
#
# Potential Improvements:
#
# - Alternative Approaches: Use a more complex structure for larger subsequences (ex: k > 3), 
#       but this approach is optimal for k = 3
#
# Edge Cases:
#
# - All elements decreasing: Returns False
# - Single valid triplet: Returns True as soon as the third element is found
# - Elements with negative values: Handled naturally by the algorithm
#

##
# While Coding
##
#
# Explanation of Greedy Algorithm Approach:
#
# 1. Initialize: first and second to infinity to track the smallest possible values for the first 
#       and second elements of the triplet
#
# 2. Iterate through each number:
#   - If the current number is less than or equal to first, update first
#   - If it's greater than first but less than or equal to second, update second
#   - If its greater than both first and second, a valid triplet exists -> return True
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = third = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                third = num
                # print(f"first = {first}; second = {second}; third = {third}")
                return True # found third element
        
        return False

def main():
    nums3 = [2,1,5,0,4,6]

    sol = Solution()

    triplet_found = sol.increasingTriplet(nums3)

    print(f"nums3 triplet_found = {triplet_found}")

    nums4 = [20,100,10,12,5,13]

    triplet_found = sol.increasingTriplet(nums4)

    print(f"nums4 triplet_found = {triplet_found}")

if __name__ == "__main__":
    main()
