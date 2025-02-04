# given an array nums, return all triplets

# Time Complexity: O(n^3): looping across array 3 times
# Space Complexity: O(n+m): we have two arrays
def ThreeSum(nums):
    result = []

    print(f"len nums = {len(nums)}")

    for i in range(len(nums)):
        # print(f"nums[i] = {nums[i]}")
        for j in range(len(nums)):
            # print(f"nums[j] = {nums[j]}")
            for k in range(len(nums)):
                # print(f"nums[k] = {nums[k]}")
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    if nums[i] + nums[j] + nums[k] == 0:
                        print(f"[{nums[i]}, {nums[j]}, {nums[k]}]")
                        result.append([nums[i], nums[j], nums[k]])
    return result

def main():
    # Example 1:
    nums = [-1, 0, 1, 2, -1, -4]
    # print(len(nums))

    result = ThreeSum(nums)

if __name__ == "__main__":
    main()
