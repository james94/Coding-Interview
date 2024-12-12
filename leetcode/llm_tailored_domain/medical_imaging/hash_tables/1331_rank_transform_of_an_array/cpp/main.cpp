#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <stdexcept>
#include <iomanip>

class MRISignalRanking {
private:
    std::vector<int> voxel_intensities;

public:
    MRISignalRanking(const std::vector<int>& intensities) : voxel_intensities(intensities) {}

    std::vector<int> rankTransform() {
        if (voxel_intensities.empty()) {
            throw std::invalid_argument("Input vector is empty");
        }

        std::unordered_map<int, int> intensity_to_rank;
        std::vector<int> unique_intensities = voxel_intensities;

        // Remove duplicates and sort
        std::sort(unique_intensities.begin(), unique_intensities.end());

        unique_intensities.erase(std::unique(unique_intensities.begin(), unique_intensities.end()), unique_intensities.end());

        // Assign ranks
        for (int i = 0; i < unique_intensities.size(); i++) {
            intensity_to_rank[unique_intensities[i]] = i + 1;
        }

        // Map intensities to ranks
        std::vector<int> result;
        result.reserve(voxel_intensities.size());
        for (int intensity : voxel_intensities) {
            result.push_back(intensity_to_rank[intensity]);
        }

        return result;
    }

    void displayMRISignalRankingResults(const std::vector<int>& ranked_intensities) {
        std::cout << "MRI Signal Intensity Ranking Results\n";
        std::cout << "Original Voxel Intensities: ";
        for (int val : voxel_intensities) {
            std::cout << std::setw(4) << val << " ";
        }

        std::cout << "\nRnaked Intensities:       ";
        for (int val : ranked_intensities) {
            std::cout << std::setw(4) << val << " ";
        }

        std::cout << "\n\n";
        std::cout << "Explanation:\n";
        std::cout << "- Rank starts from 1\n";
        std::cout << "- Higher intensities receive higher ranks\n";
        std::cout << "- Equal intensities have the same rank\n";
        std::cout << "- Ranks are compact (no skipped numbers)\n";
        std::cout << "This ranking is crucial for MRI post-processing techniques.\n\n";
    }
};

int main() {
    std::cout << "MRI Signal Intensity Ranking\n";
    std::cout << "============================\n\n";
    std::cout << "This software module ranks voxel intensities in a 3D MRI volume.\n";
    std::cout << "It's essential for various post-processing techniques, including\n";
    std::cout << "image segmentation and feature extraction.\n\n";

    std::vector<std::vector<int>> test_cases = {
        {40, 10, 20, 30},
        {100, 100, 100},
        {37, 12, 28, 9, 100, 56, 80, 5, 12}
    };

    for (const auto& test_case : test_cases) {
        MRISignalRanking ranker(test_case);
        std::vector<int> result;
        try {
            result = ranker.rankTransform();
            ranker.displayMRISignalRankingResults(result);
            // std::cout << "Input: ";
            // for (int val : test_case) {
            //     std::cout << val << " ";
            // }

            // std::cout << "\nOutput: ";
            // for (int val : result) {
            //     std::cout << val << " ";
            // }
            // std::cout << "\n\n";

        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }

    return 0;
}
