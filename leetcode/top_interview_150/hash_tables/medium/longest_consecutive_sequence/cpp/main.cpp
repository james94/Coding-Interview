#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

/**
**Leetcode Hash Table Questions:**

- https://leetcode.com/problem-list/hash-table/

**Leetcode Problem:**

- https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=hash-table

**ChatGPT solution:**

- https://chatgpt.com/share/66e796dd-2f74-8005-aa4a-a12386fcfe25

*/

/**
Approach: Longest Consecutive Sequence in C++ using Hash Set

Step 1: Create a hash set for fast lookup
    - store all elements in the set
    - this allows us to check if an element is part of the sequence in O(1) time

Step 2: Check for Sequence Start
    - for each element, check if it is the start of a sequence by ensuring num-1 is not in the set
        - a start of a sequence is an element that has no previous element in the set
    - this ensures we only start counting when we encounter the first element of a sequence

Step 3: Count the Sequence Length
    - for each start of a sequence, count the length of the sequence by checking num+1, num+2, ... in the set
    - increment the length until we reach the end of the sequence

Step 4: Track the Longest Sequence
    - keep track of the longest sequence length encountered

*/

/**
// Time Complexity: O(n)
    - where n is the number of elements in the array
    - we process each element once via constant-time operation
// Space Complexity: O(n)
    - we use a hash set to store the elements
*/
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Edge case: empty array
        if (nums.size() == 0) {
            return 0;
        }

        // Create a hash set to store all elements of the array
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longestStreak = 0;

        // Traverse through the elements of the array
        for (int num : numSet) {
            // Check if the element is the start of a sequence
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentStreak = 1;

                // Count the length of the consecutive sequence
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum++;
                    currentStreak++;
                }

                // Update the longest sequence length streak
                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
};

void printArray(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}

int main() {
    Solution solution;

    vector<int> nums1 = {100, 4, 200, 1, 3, 2};
    vector<int> nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};

    cout << "Vector nums1: ";
    printArray(nums1);
    cout << "Longest Consecutive Sequence in nums1: " << solution.longestConsecutive(nums1) << endl;

    cout << "Vector nums2: ";
    printArray(nums2);
    cout << "Longest Consecutive Sequence in nums2: " << solution.longestConsecutive(nums2) << endl;
    return 0;
}