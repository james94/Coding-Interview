#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    // Time Complexity O(n): n is number of trees. We iterate through the
    // array once with the right poniter and the left poniter never moves
    // more than n times in total

    // Space Complexity O(1): we use a hash map that stores at most 3 entries
    // (2 fruit types in current window and 1 that we're removing)
    int totalFruit(std::vector<int>& fruits) {
        // store fruit types (key) and their counts (value)
        std::unordered_map<int, int> basket;

        // Implement two pointers for sliding window technique
        int left = 0, maxFruits = 0;

        for (int right = 0; right < fruits.size(); ++right) {
            // Add current fruit into basket or increment its count
            basket[fruits[right]]++;

            // If two or more than 2 types of fruits in the basket
            while (basket.size() > 2) {
                // We start removing fruits from left side of window
                // until only 2 types
                if (--basket[fruits[left]] == 0) {
                    basket.erase(fruits[left]);
                }
                left++;
            }

            // Update maxFruits with max window size encountered 
            maxFruits = std::max(maxFruits, right - left + 1);
        }

        return maxFruits;
    }
};

int main() {
    Solution solution;

    // Example 1
    std::vector<int> fruits1 = {1, 2, 1};
    std::cout << "Example 1 Output: " << solution.totalFruit(fruits1) << std::endl;

    // Example 2
    std::vector<int> fruits2 = {0, 1, 2, 2};
    std::cout << "Example 2 Output: " << solution.totalFruit(fruits2) << std::endl;

    // Example 3
    std::vector<int> fruits3 = {1, 2, 3, 2, 2};
    std::cout << "Example 3 Output: " << solution.totalFruit(fruits3) << std::endl;
    return 0;
}
