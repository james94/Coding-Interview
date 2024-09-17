// 80. Remove Duplicates from Sorted Array II
//
// Leetcode Problem: 
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

// Perplexity.ai solution:
// https://www.perplexity.ai/search/you-are-a-coding-interview-ass-nORHwUVmThuH673K060Y4Q

// ChatGPT solution:
// https://chatgpt.com/share/66e65181-0e8c-8005-961b-ed3de4257d94

#include <vector>
#include <iostream>

// Time Complexity: O(n)
// where n is length of array as we traverse it once

// Space Complexity: O(1)
// we only use a few extra variables
int removeDuplicates(std::vector<int>& nums) {
    if (nums.size() <= 2) {
        return nums.size();
    }

    int index = 2; // Start at 2 since criteria allows up to 2 duplicates

    for (int i = 2; i < nums.size(); i++) {
        if (nums[i] != nums[index - 2]) {
            nums[index] = nums[i];
            index++;
        }
    }

    return index;
}

int main() {
    std::vector<int> nums1 = {1, 1, 1, 2, 2, 3};
    int k1 = removeDuplicates(nums1);

    std::cout << "Result k1: " << k1 << ", Modified Array: ";
    for(int i = 0; i < k1; i++) {
        std::cout << nums1[i] << " ";
    }
    std::cout << std::endl;

    std::vector<int> nums2 = {0, 0, 1, 1, 1, 1, 2, 3, 3};
    int k2 = removeDuplicates(nums2);

    std::cout << "Result k2: " << k2 << ", Modified Array: ";
    for(int i = 0; i < k2; i++) {
        std::cout << nums2[i] << " ";
    }
    std::cout << std::endl;


    return 0;
}
