#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

class Solution {
public:
    std::string licenseKeyFormatting(std::string s, int k) {
        std::string result;
        // Pre-allocate memory
        result.reserve(s.length() + s.length() / k);

        // Remove dashes and convert to uppercase
        auto it = std::copy_if(s.rbegin(), s.rend(), std::back_inserter(result),
            [](char c) {
                return c != '-';
            }
        );

        std::transform(result.begin(), result.end(), result.begin(),
            [](unsigned char c) {
                return std::toupper(c);
            }
        );

        // Insert dashes
        for (int i = k; i < result.length(); i += k + 1) {
            result.insert(result.begin() + i, '-');
        }

        std::reverse(result.begin(), result.end());
        return result;
    }

};

int main() {
    Solution solution;

    // Example 1
    std::string s1 = "5F3Z-2e-9-w";
    int k1 = 4;
    std::cout << "Example 1 Output: " << solution.licenseKeyFormatting(s1, k1) << std::endl;


    // Example 2
    std::string s2 = "2-5g-3-J";
    int k2 = 2;
    std::cout << "Example 2 Output: " << solution.licenseKeyFormatting(s2, k2) << std::endl;



    return 0;
}
