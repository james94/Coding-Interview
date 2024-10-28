#include <iostream>
#include <unordered_map>
#include <vector>
#include <iomanip>
#include <string>
#include <string_view>
#include <type_traits>

// 10:22PM - 10:37PM

// 13. Roman To Integer
// Leetcode: https://leetcode.com/problems/roman-to-integer/description/?envType=company&envId=google&favoriteSlug=google-all&difficulty=EASY

int RomanToInteger(const std::string romans) {
    int result = 0;
    std::unordered_map<char, int> roman_ch_to_int{
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
    };
    std::unordered_map<std::string, int> roman_str_to_int{
        {"IV", 4}, {"IX", 9},  {"XL", 40}, {"XC", 90},  {"CD", 400}, {"CM", 900},
    };

    for (int i = 0; i < romans.size(); i++) {
        if (romans.find("IV", i) == i && romans.find("IV", i) != std::string::npos) {
            result += roman_str_to_int["IV"];
            i++;
        }
        else if (romans.find("IX", i) == i && romans.find("IX", i) != std::string::npos) {
            result += roman_str_to_int["IX"];
            i++;
        }
        else if (romans.find("XL", i) == i &&romans.find("XL", i) != std::string::npos) {
            result += roman_str_to_int["XL"];
            i++;
        }
        else if (romans.find("XC", i) == i && romans.find("XC", i) != std::string::npos) {
            result += roman_str_to_int["XC"];
            i++;
        }
        else if (romans.find("CD", i) == i && romans.find("CD", i) != std::string::npos) {
            result += roman_str_to_int["CD"];
            i++;
        }
        else if (romans.find("CM", i) == i && romans.find("CM", i) != std::string::npos) {
            result += roman_str_to_int["CM"];
            i++;
        }
        else {
            std::cout << roman_ch_to_int[romans[i]] << std::endl;
            result += roman_ch_to_int[romans[i]];
        }
    }
    return result;
}

int main() {
    std::string romans1{"III"};
    std::cout << "Romans1 To Integer: " << RomanToInteger(romans1) << "\n";

    std::string romans3{"MCMXCIV"};
    std::cout << "Romans3 To Integer: " << RomanToInteger(romans3) << "\n";

    return 0;
}