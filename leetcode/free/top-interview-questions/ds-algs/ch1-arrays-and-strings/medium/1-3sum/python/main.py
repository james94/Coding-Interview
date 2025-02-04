# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#0

def threeSum(nums):
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