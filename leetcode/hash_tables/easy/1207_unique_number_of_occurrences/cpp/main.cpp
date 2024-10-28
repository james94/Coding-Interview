#include <iostream>
#include <vector>

#include <unordered_map>

// 1207. Unique Number of Occurrences
// Leetcode Problem: https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

// Time Period: 11:40PM - 12AM; 12:56AM: 1 hour 16 mins

// C++ API Unordered Map Reference: https://en.cppreference.com/w/cpp/container/unordered_map
// C++ Unordered MultiMap Reference: https://en.cppreference.com/w/cpp/container/unordered_multimap/count

bool HasOnlyUniqueNumberOccurrences(const std::vector<int> arr) {
    std::unordered_multimap<int, int> arr_map_dupkeys_occurrences, arr_map_dupkeys_occs_res;
    std::unordered_map<int, int> arr_map_ukeys_occurrences;

    bool only_unique_num_occurrences = false;

    for (int i = 0; i < arr.size(); i++) {
        arr_map_dupkeys_occurrences.emplace(arr[i], arr[i]);

    }

    std::cout << "Unordered Map Duplicate Keys, Help Find Occurrences:\n";
    for (auto const& [key, value] : arr_map_dupkeys_occurrences) {
        std::cout << "Key: [" << key << "] Value: [" << value << "]\n";
        arr_map_ukeys_occurrences.emplace(key, arr_map_dupkeys_occurrences.count(key));
    }

    std::cout << "Unordered MultiMap Unique Keys with Occurrences:\n";
    for (auto const& [key, value] : arr_map_ukeys_occurrences) {
        std::cout << "Key: [" << key << "] Value: [" << value << "]\n";

        // value is the number of occurrences of the unique key, which we got from our first multimap
        if (auto search_dup_occur = arr_map_dupkeys_occs_res.find(value); search_dup_occur != arr_map_dupkeys_occs_res.end()) {
            std::cout << "Found Occurrences of '" << value << "' for Key '" << key << "' isnt unique because theres already another key with those number of occurrences!" << std::endl;
            only_unique_num_occurrences = false;
            break;
        }
        arr_map_dupkeys_occs_res.emplace(value, key);
        only_unique_num_occurrences = true;
    }

    return only_unique_num_occurrences;
}

int main() {
    // Given array of integers
    // std::vector<int> arr1{1, 2, 2, 1, 1, 3};
    std::vector<int> arr1{1, 2};

    // Create a function that takes vector, returns true if number of occurrences
    // of each value in the array is unique, else return false
    bool only_unique_occurrences = HasOnlyUniqueNumberOccurrences(arr1);

    std::string only_unique_occurrences_res = only_unique_occurrences ? "Yes" : "No";

    std::cout << "arr1 only has unique occurrences?: " << only_unique_occurrences_res << std::endl;

    return 0;
}