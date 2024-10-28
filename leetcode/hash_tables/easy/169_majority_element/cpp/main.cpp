// Time Period: 8:50AM -9:05AM:
// 169. Majority Element
// Leetcode Ref: https://leetcode.com/problems/majority-element/description/?envType=company&envId=google&favoriteSlug=google-all&difficulty=EASY

#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>

// The majority element is the element that appears more than n/2 times
// You can assume the majority element always exists in the array
int MajorityElement(std::vector<int>& nums) {
    // std::unordered_multimap<int, int> nums_map;
    // std::map<int, int> nums_elm_occurs_map;
    // int majority_element = 0;

    // for (int i = 0; i < nums.size(); i++) {
    //     nums_map.emplace(nums[i], i);
    // }
    // // you can get the count of occurrences per element
    // for (const auto& [key, value] : nums_map) {
    //     nums_elm_occurs_map.emplace(nums_map.count(key), key);
    // }
    // // determine majority element with most occurrences via reverse iterator descending
    // for (auto it = nums_elm_occurs_map.crbegin(); it != nums_elm_occurs_map.crend(); ++it) {
    //     std::cout << "Majority Element: [" << it->second << "] Occurrences: [" << it->first << "]\n";
    //     majority_element = it->second;
    //     break;
    // }
    // return majority_element;

    std::sort(nums.begin(), nums.end());

    return nums[nums.size()/2];
}


int main() {
    // Given array `nums` of size `n`
    std::vector<int> nums1{3,2,3};

    // Return majority element
    std::cout << "Nums1 - Majority Element: " << MajorityElement(nums1) << "\n";

    std::vector<int> nums2{2,2,1,1,1,2,2};
    std::cout << "Nums2 - Majority Element: " << MajorityElement(nums2) << "\n";
    return 0;
}