from typing import List

# 15 - 6 = 9 mins: finished algorithm


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # sorted_nums = nums.sort()

        i = 0
        j = 1
        k = 2

        n = len(nums)

        while i < n and j < n and k < n:
            print(f"i = {i}; j = {j}; k = {k}")
            if i < j < k and nums[i] < nums[j] < nums[k]:
                return True

            i += 1
            j += 1
            k += 1

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
