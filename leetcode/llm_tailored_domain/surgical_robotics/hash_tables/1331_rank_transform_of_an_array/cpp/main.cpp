#include <vector>
#include <algorithm>
#include <unordered_map>

class SurgicalRobotRanking {
public:
    std::vector<int> rankPrecisionReadings(std::vector<int>& precisionReadings) {
        std::vector<int> sortedReadings = precisionReadings;
        std::sort(sortedReadings.begin(), sortedReadings.end());

        std::unordered_map<int, int> rankMap;
        int rank = 0;

        for (int reading : sortedReading) {
            if (rankMap.find())
        }

    }


};
