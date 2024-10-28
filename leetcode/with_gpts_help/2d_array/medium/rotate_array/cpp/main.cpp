#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// **Leetcode Problem:**

// - https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

// **ChatGPT solution:**

// - https://chatgpt.com/share/66e69e8b-9230-8005-a527-8a34bdf74fa6

// Rotate Array Brief Description:
// Rotating Right: elements are shifted to the right and the elements
// that go off the end are brought back to the beginning

// In-place rotation: we modify the array in place without using extra space


// Rotate Array Approach 1:

// Time Complexity: O(n)
// reversing the array takes O(n) time and reversing the first k elements and 
// the remaining elements takes O(k) and O(n-k) time respectively

// Space Complexity: O(1)
// we only use a few extra variables (constant space)
void multi_reverses_rotate(vector<int>& nums, int k) {
    // If k is greater than the size of the array, we can just take the modulo
    k = k % nums.size();
    // Step 1: Reverse the entire array
    reverse(nums.begin(), nums.end());
    // Step 2: Reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    // Step 3: Reverse the remaining elements
    reverse(nums.begin() + k, nums.end());
}

void rotate_array_approach1() {
    cout << "Rotate Array Approach 1: Multi-Reverses Rotation" << endl;
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    int k1 = 3;
    multi_reverses_rotate(nums1, k1);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;

    vector<int> nums2 = {-1, -100, 3, 99};
    int k2 = 2;
    multi_reverses_rotate(nums2, k2);
    for (int i = 0; i < nums2.size(); i++) {
        cout << nums2[i] << " ";
    }
    cout << endl;
}

// Rotate Array Approach 2:
// We use Cyclic Replacements to rotate the array in place
// - We rotate the elemets one by one following a cycle
// - We start at index 0, move the element at index 0 to its new position (0 + k) % n,
//   then move the element at the new position to its correct position, and so on
// - Once we finish a cycle, we move to the next element and repeat the process

// Time Complexity: O(n)
// - each element is moved exactly once, and we process all n elements

// Space Complexity: O(1)
// - we use only constant extra space for variables like count, current, prev, etc
void cyclic_replacements_rotate(vector<int>& nums, int k) {
    // In case k is larger than the array size
    k = k % nums.size();
    // To track the number of elements that have been rotated
    int count = 0;

    // We start at the beginning of the array index 0 and keep rotating elements
    for (int start = 0; count < nums.size(); start++) {
        int current = start;
        int prev = nums[start];

        do {
            // Calculate the next index position to rotate element to
            int next = (current + k) % nums.size();
            // Swap the current element with the element at the new index position
            int temp = nums[next];
            nums[next] = prev;
            prev = temp;

            // Move to the next element index
            current = next;
            // Increment the count of elements rotated
            count++;
            // Continue rotating elements until we reach the starting index, completing a cycle
                // then we move to the next unprocessed element and repeat process
        } while (start != current);
    }
}

void rotate_array_approach2() {
    cout << "Rotate Array Approach 2: Cyclic Replacements Rotation" << endl;
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    int k1 = 3;
    cyclic_replacements_rotate(nums1, k1);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;

    vector<int> nums2 = {-1, -100, 3, 99};
    int k2 = 2;
    cyclic_replacements_rotate(nums2, k2);
    for (int i = 0; i < nums2.size(); i++) {
        cout << nums2[i] << " ";
    }
    cout << endl;
}

int main() {
    // Multi-Reverses Rotation Approach 1: reversing the array and then reversing the first k elements and the remaining elements
    rotate_array_approach1();

    // Cyclic Replacements Rotation Approach 2: avoids reversing the array
    rotate_array_approach2();

    return 0;
}
