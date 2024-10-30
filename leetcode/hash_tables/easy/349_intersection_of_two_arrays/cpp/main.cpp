#include <iostream>
#include <vector>
#include <unordered_map>
// 10:06PM -10:34PM: 28 mins

// 349. Intersection of Two Arrays
// Leetcode: https://leetcode.com/problems/intersection-of-two-arrays/?envType=company&envId=google&favoriteSlug=google-all&difficulty=EASY

std::vector<int> ArraysIntersect(const std::vector<int>& nums1, const std::vector<int>& nums2) {
    std::unordered_map<int, int> nums1_map;
    std::unordered_map<int, int> nums2_map;
    std::vector<int> intersect_res;

    for (int i = 0; i < nums1.size(); i++) {
        nums1_map.emplace(nums1[i], i);
    }

    for (int i = 0; i < nums2.size(); i++) {
        nums2_map.emplace(nums2[i], i);
    }

    if (nums1_map.size() < nums2_map.size()) {
        for(const auto [nums1_key, nums1_value] : nums1_map) {
            if (auto search = nums2_map.find(nums1_key); search != nums2_map.end()) {
                std::cout << "Found Nums1 & Nums2 Intersection: " << search->first << "\n";
                intersect_res.push_back(search->first);
            }
        }
    }
    else {
        for(const auto [nums2_key, nums2_value] : nums2_map) {
            if (auto search = nums1_map.find(nums2_key); search != nums1_map.end()) {
                std::cout << "Found Nums1 & Nums2 Intersection: " << search->first << "\n";
                intersect_res.push_back(search->first);
            }
        }
    }

    return intersect_res;

}

int main() {
    // Ex:
    std::vector<int> nums1{1,2,2,1};
    std::vector<int> nums2{2,2};

    std::cout << "Nums1 & Nums2 Arrays Intersect:\n";
    std::vector<int> nums_intersect = ArraysIntersect(nums1, nums2);

    for (int i = 0; i < nums_intersect.size(); i++) {
        std::cout << nums_intersect[i] << " ";
    }
    std::cout << "\n";

    std::vector<int> nums3{4,9,5};
    std::vector<int> nums4{9,4,9,8,4};

    std::cout << "Nums3 & Nums4 Arrays Intersect:\n";
    std::vector<int> nums_intersect2 = ArraysIntersect(nums3, nums4);

    for (int i = 0; i < nums_intersect2.size(); i++) {
        std::cout << nums_intersect2[i] << " ";
    }
    std::cout << "\n";

    return 0;
}