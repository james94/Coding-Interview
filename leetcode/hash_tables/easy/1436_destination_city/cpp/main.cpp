#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

// Time Period: 7:54AM - 8: 14AM; Laid Back Focus = 7:15PM - 8:56PM
    // Deep Focus: 8:56PM - 10:04PM
        // NOTE: (Erased FindDestinationCity code, started over)

// 1436. Destination City
// Leetcode Problem: https://leetcode.com/problems/destination-city/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

// We can store keys in unordered hash map with unique keys, so our last key is destination city
std::string FindDestinationCity(const std::vector<std::vector<std::string>>& paths) {
    std::unordered_multimap<std::string, std::string> city_path_dest_map;
    std::string curr_dest_city, next_dest_city;

    for (int i = 0; i < paths.size(); i++) {
        city_path_dest_map.emplace(paths[i][0], paths[i][1]);
    }

    curr_dest_city = paths[0][0];
    for (int i = 0; i < city_path_dest_map.size(); i++) {
        if (auto search = city_path_dest_map.find(curr_dest_city); search != city_path_dest_map.end()) {
            std::cout << search->first << " -> " << search->second << std::endl;
            if (curr_dest_city == search->first) {
                next_dest_city = search->second;
            }
            curr_dest_city = next_dest_city;
        }
    }

    return curr_dest_city;
}

int main() {
    // given paths array
        // [cityA, cityB] means exists direct path from cityA to cityB
        // return destination city, which is the city without any path outgoing to another city
        // Trip: London -> New York -> Lima -> Sao Paulo
    std::vector<std::vector<std::string>> paths1{
        {"London", "New York"}, {"New York", "Lima"}, {"Lima", "Sao Paulo"}
    };

    std::cout << "Paths1 - Destination City: " << FindDestinationCity(paths1) << std::endl;

    // Ex: 2: (Trip1) B -> C -> A
        // (Trip2) D -> B -> C -> A... etc
    std::vector<std::vector<std::string>> paths2{
        {"B", "C"}, {"D", "B"}, {"C", "A"}
    };

    std::cout << "Paths2 - Destination City: " << FindDestinationCity(paths2) << std::endl;

    // Ex3: Trip: kzwEQHfwce -> pYyNGfBYbm -> wxAscRuzOl
    std::vector<std::vector<std::string>> paths3{
        {"pYyNGfBYbm","wxAscRuzOl"},{"kzwEQHfwce","pYyNGfBYbm"}
    };
    // Exp Res: "wxAscRuzOl"

    std::cout << "Paths3 - Destination City: " << FindDestinationCity(paths3) << std::endl;

    std::vector<std::vector<std::string>> paths4{
        {"qMTSlfgZlC","ePvzZaqLXj"}, {"xKhZXfuBeC","TtnllZpKKg"}, {"ePvzZaqLXj","sxrvXFcqgG"},
        {"sxrvXFcqgG","xKhZXfuBeC"}, {"TtnllZpKKg","OAxMijOZgW"}
    };

    std::cout << "Paths4 - Destination City: " << FindDestinationCity(paths4) << std::endl;

    return 0;
}