#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

// Google Interview Process Leetcode Question "Unique Email Addresses": https://leetcode.com/explore/interview/card/google/67/sql-2/3044/

class Solution {
public:
    int numUniqueEmails(std::vector<std::string>& emails) {
        std::unordered_set<std::string> uniqueEmails;

        for (const auto& email : emails) {
            std::string normalizedEmail = normalizeEmail(email);
            uniqueEmails.insert(normalizedEmail);
        }

        return uniqueEmails.size();
    }

private:
    std::string normalizeEmail(const std::string& email) {
        std::string result;
        bool ignoreLocal = false;
        bool isDomain = false;

        for (char c : email) {
            if (isDomain) {
                result += c;
            }
            else if (c == '@') {
                isDomain = true;
                result += c;
            } else if (!ignoreLocal) {
                if (c == '.') {
                    continue;
                }
                if (c == '+') {
                    ignoreLocal = true;
                    continue;
                } 

                result += c;
            }
        }

        return result;
    }

};

int main() {
    Solution solution;

    std::vector<std::string> emails1 = {"test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"};

    std::vector<std::string> emails2 = {"a@leetcode.com",
        "b@leetcode.com", "c@leetcode.com"};

    std::cout << "Example 1 Output: " << solution.numUniqueEmails(emails1) << std::endl;

    std::cout << "Example 2 Output: " << solution.numUniqueEmails(emails2) << std::endl;
    
    return 0;
}
