#include <iostream>
#include <string>
#include <unordered_map>

// Time: 11:16PM - 12:03AM: 47 mins (also making food in between)

// 242. Valid Anagram
// Leetcode: https://leetcode.com/problems/valid-anagram/description/?envType=company&envId=apple&favoriteSlug=apple-all&difficulty=EASY

bool ValidAnagram(const std::string& s1, const std::string& t1) {
    std::unordered_multimap<char, int> s1_dupkey_occurs_map, t1_dupkey_occurs_map;
    std::unordered_map<char, int> s1_ukey_occurs_map, t1_ukey_occurs_map;
    bool found_anagram = true;

    if (s1.size() != t1.size()) {
        found_anagram = false;
        return found_anagram;
    }

    for(int i = 0; i < s1.size(); i++) {
        s1_dupkey_occurs_map.emplace(s1[i], i);
    }

    for(int i = 0; i < t1.size(); i++) {
        t1_dupkey_occurs_map.emplace(t1[i], i);
    }

    for (auto const& [key, value] : s1_dupkey_occurs_map) {
        s1_ukey_occurs_map.emplace(key, s1_dupkey_occurs_map.count(key));
    }

    for (auto const& [key, value] : t1_dupkey_occurs_map) {
        t1_ukey_occurs_map.emplace(key, t1_dupkey_occurs_map.count(key));
    }

    for (auto const& [t1_key, t1_value] : t1_ukey_occurs_map) {
        if (auto search = s1_ukey_occurs_map.find(t1_key); search != s1_ukey_occurs_map.end()) {
            std::cout << "Found S1 & T1 Matching Key: " << search->first << "\n";
            if (t1_value != search->second) {
                std::cout << "Invalid Anagram: T1 & S1 Key Occurrences Not Equal: \n";
                std::cout << "S1 Key Occurrences: " << search->second << "\n";
                std::cout << "T1 Key Occurrences: " << t1_value << "\n";
                found_anagram = false;
                break;
            }
        }
        else {
            std::cout << "Invalid Anagram: Couldnt Find t1_key: " << t1_key << " in s1_ukey_occurs_map\n";
            found_anagram = false;
            break;
        }
    }

    return found_anagram;
}

int main() {
    std::string s1 = "anagram";
    std::string t1 = "nagaram";

    bool is_anagram = ValidAnagram(s1, t1);

    std::string anagram_res = is_anagram ? "Valid" : "Invalid";

    std::cout << anagram_res << " Anagram\n";

    return 0;
}