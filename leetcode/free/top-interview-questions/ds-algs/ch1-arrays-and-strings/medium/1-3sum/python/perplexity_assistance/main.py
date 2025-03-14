# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#0

####
#   Data Structures & Algorithm Concepts
####
#
#   Sorting: the problem can be approached by sorting the input array, which allows for efficient searching of triplets
#
#   Two-Pointers Techniques: useful for finding pairs within a sorted array that sum up to a target value
#
####
#   Clarifying Questions
####
#
#   Are there any constraints on the input array size or the range of integers?
#
#   How should duplicate triplets be handled?
#
####
#   Potential Solutions
#### 
#
#   Brute Force: Checking all possible triplets, which has a time complexity of O(n^3)
#
#   Optimized Solution: Sorting the array and using the two-pointers technique to
#    # achieve a time complexity of O(n^2
#
####
#   Explanation
####
#
#   Sorting
#
#   Two-Pointers Technique
#
#   Handling Duplicates: skips duplicate triplets by checking if the current element is the same as the previous one
#
####
#   Big O Notation
####
#
#   Time Complexity: O(n^2), which is optimal for this problem using Two-Pointers technique
#
#   Space Complexity: O(n) for storing the result, can be optimized if needed by returning an iterator instead of a list

def threeSum(nums):
    # sorted: -4, -1, -1, 0, 1, 2
    nums.sort()

    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                # Move left pointer to increase sum
                left += 1
            elif total > 0:
                # Move right pointer to decrease sum
                right -= 1
            else:
                # Found a triplet, add it to result and skip duplicates
                print(f"[{nums[i]}, {nums[left]}, {nums[right]}]")
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    return result

def main():
    nums = [-1,0,1,2,-1,-4]
    result = threeSum(nums)


if __name__ == "__main__":
    main()