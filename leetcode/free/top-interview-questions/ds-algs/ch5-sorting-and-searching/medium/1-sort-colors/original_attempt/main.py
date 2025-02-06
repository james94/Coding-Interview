def sort_inplace(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if left > right:
            nums[left] = temp_left
            nums[left] = nums[right]
            nums[right] = temp_left

        left += 1
        right -= 1
        
    print(nums)

def main():
    # 0, 1, and 2 to represent the color red, white, and blue
    nums = [2,0,2,1,1,0]

    sort_inplace(nums)

if __name__ == "__main__":
    main()
