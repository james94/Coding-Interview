#include <iostream>
#include <string>
#include <unordered_map>

// Oct 28; 12:31AM - 12:41AM:
    // Oct 29; 7:58PM - 8:42PM:

// 387. First Unique Character in a String
// Leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=company&envId=apple&favoriteSlug=apple-all&difficulty=EASY
int FirstUniqueCharacterPos(const std::string& s1) {
    std::unordered_map<char, int> s1_ukey_occurs_map;

    for (int i = 0; i < s1.size(); i++) {
        s1_ukey_occurs_map[s1[i]] += 1;
    }

    for (int i = 0; i < s1.size(); i++) {
        if (s1_ukey_occurs_map[s1[i]] == 1) {
            return i;
        }
    }

    return -1;
}

int main() {
    // Given string s1
    std::string s1 = "leetcode";

    // Find First Non-Repeating Character in s1, return its index
    int first_unique_char_pos = FirstUniqueCharacterPos(s1);

    std::cout << "First Unique Character Position: " << first_unique_char_pos << "\n";
    return 0;
}