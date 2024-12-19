#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <algorithm>

// We'll use a combination of dynamic programming and a montonic stack
class Solution {
public:
    int oddEvenJumps(std::vector<int>& arr) {
        int n = arr.size();
        
        if (n <= 1) {
            return n;
        }

        std::vector<bool> odd(n, false);
        std::vector<bool> even(n, false);
        odd[n-1] = even[n-1] = true;

        std::map<int, int> valueToIndex;
        valueToIndex[arr[n-1]] = n-1;

        int goodIndices = 1;

        for (int i = n-2; i >= 0; --i) {
            auto oddJump = valueToIndex.lower_bound(arr[i]);
            auto evenJump = valueToIndex.upper_bound(arr[i]);

            if (oddJump != valueToIndex.end()) {
                odd[i] = even[oddJump->second];
            }
            if (evenJump != valueToIndex.begin()) {
                even[i] = odd[(--evenJump)->second];
            }

            if (odd[i]) {
                ++goodIndices;
            }

            valueToIndex[arr[i]] = i;
        }

        return goodIndices;
    }
};

int main() {
    Solution solution;

    // Example 1
    std::vector<int> arr1 = {10, 13, 12, 14, 15};
    std::cout << "Example 1 Output: " << solution.oddEvenJumps(arr1) << std::endl;

    // Example 2
    std::vector<int> arr2 = {2, 3, 1, 1, 4};
    std::cout << "Example 2 Output: " << solution.oddEvenJumps(arr2) << std::endl;

    // Example 3
    std::vector<int> arr3 = {5, 1, 3, 4, 2};
    std::cout << "Example 3 Output: " << solution.oddEvenJumps(arr3) << std::endl;

    return 0;
}
