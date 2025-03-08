# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-Je6PtfnLTsu.hvXrYVTNzQ#0

####
#   Data Structures & Algorithm Concepts
####
#
#   Potential Algorithms/Solutions:
#
#   Three-Pointer Technique: approach for this problem is to use three pointers to track the positions of the next red,
#       white, and blue elements
#
#   Counting Sort: since there are only three distinct values, counting sort could be an efficient solution.
#
####
#   Clarifying Questions
####
#
#   Are there any constraints on the input size or the range of values?
#
#   Can we use extra space? The follow-up question asks for a solution using only constant extra space.
#
####
#   Big O Notation
####
#
#   Time Complexity: Current solution O(n), which is optimal for this problem
#
#   Space Complexity: uses constant extra space O(1), meeting the follow-up requirement
#

# We'll use Three-Pointer Technique to sort colors
def sortColors(nums):
    # Initialize pointers for the next positions of 0 and 2
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
        # if the current element is 0, swap it with the element at the left pointer
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        # if the current element is 2, swap it with the element at the right pointer
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        # if the current element is 1, just move to the next element
        else:
            i += 1

def main():
    # 0, 1, and 2 to represent the color red, white, and blue
    nums = [2,0,2,1,1,0]

    sortColors(nums)

    # since we sorted array in-place, its like pass by reference in C++
    print(nums)

if __name__ == "__main__":
    main()

