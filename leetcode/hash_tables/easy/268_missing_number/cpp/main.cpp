#include <iostream>

#include <unordered_map>
#include <vector>

// 268. Missing Number
// Leetcode Ref: https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

// Time Period: 9:21PM - 9:41PM; 9:56PM: 35 mins
// C++ Unordered Map Reference: https://en.cppreference.com/w/cpp/container/unordered_map/find

// 268. Missing Number
int FindMissingNumber(const std::vector<int>& nums) {
    int nums_size = nums.size(); // tells us how many distinct numbers "n" in vector

    std::unordered_map<int, int> nums_map_res;

    int missing_number = -1;

    for (int i = 0; i < nums.size(); i++) {
        nums_map_res.emplace(nums[i], 1);
    }

    for (int i = 0; i <= nums.size(); i++) {
        if (auto search = nums_map_res.find(i); search != nums_map_res.end()) {
            std::cout << "Found: " << search->first << " " << search->second << std::endl;
        }
        else {
            std::cout << "Missing Number: " << i << " " << std::endl;
            missing_number = i;
            break;
        }
    }
    return missing_number;
}

// Prompt given
int main() {
    // Given nums containing "n" distinct numbers
    // in range [0, n], return the only number in
    // range that is missing from the array

    // Ex 1:
    std::vector<int> nums1{3, 0, 1};
    int missing_number = FindMissingNumber(nums1);
    return 0;
}