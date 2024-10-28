#include <iostream>

// Check cppref
#include <unordered_map>
#include <vector>

// 217. Contains Duplicate
// Link: https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

// Prompt: Given integer array `nums`
// Return `true` if any value appears "at least twice" in array
// Return `false` if every element is distinct

// Time: 6:35 - 6:57PM: 22 mins about?
// C++ Unordered MultiMap Reference: https://en.cppreference.com/w/cpp/container/unordered_multimap/count

bool ContainsDuplicate(const std::vector<int>& nums) {
    std::unordered_multimap<int, int> nums_map;

    for (int i = 0; i < nums.size(); i++) {
        nums_map.emplace(nums[i], nums[i]);
    }

    for (int i = 0; i < nums.size(); i++) {
        if (nums_map.count(nums[i]) > 1) {
            std::cout << "Duplicate: " << nums[i] << std::endl;
            return true;
        }
    }
    return false;
}

int main() {
    // Example 1:
    std::vector<int> nums1{1, 2, 3, 1};

    std::cout << "Nums1: Contains Duplicate?: " << ContainsDuplicate(nums1) << std::endl;
    return 0;
}