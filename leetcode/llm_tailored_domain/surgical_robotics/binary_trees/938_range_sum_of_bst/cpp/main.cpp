#include <iostream>
#include <atomic>
#include <mutex>
#include <vector>

class SurgicalInstrumentTracker {
private:
    struct TreeNode {
        int distance;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int x) : distance(x), left(nullptr), right(nullptr) {}
    };

    TreeNode* root;
    std::mutex treeMutex;

    TreeNode* insertRec(TreeNode* node, int distance) {
        if (node == nullptr) {
            return new TreeNode(distance);
        }

        if (distance < node->distance) {
            node->left = insertRec(node->left, distance);
        }

        else if (distance > node->distance) {
            node->right = insertRec(node->right, distance);
        }

        return node;
    }



    void getAllDistancesRec(TreeNode* node, std::vector<int>& distances) {
        if (node == nullptr) {
            return;
        }

        getAllDistancesRec(node->left, distances);
        distances.push_back(node->distance);
        getAllDistancesRec(node->right, distances);
    }

    int sumInRangeRec(TreeNode* node, int min_distance, int max_distance) {
        if (node == nullptr) {
            return 0;
        }

        if (node->distance >= min_distance && node->distance <= max_distance) {
            return node->distance + sumInRangeRec(node->left, min_distance, max_distance) + 
                                    sumInRangeRec(node->right, min_distance, max_distance);
        }
        else if (node->distance < min_distance) {
            return sumInRangeRec(node->right, min_distance, max_distance);
        }
        else {
            return sumInRangeRec(node->left, min_distance, max_distance);
        }
    }

public:
    SurgicalInstrumentTracker() : root(nullptr) {}

    void insert(int distance) {
        std::lock_guard<std::mutex> lock(treeMutex);
        root = insertRec(root, distance);
    }

    int sumInRange(int min_distance, int max_distance) {
        std::lock_guard<std::mutex> lock(treeMutex);
        return sumInRangeRec(root, min_distance, max_distance);
    }

    // Helper function to get all values in the tree (for demonstration purposes)
    std::vector<int> getAllDistances() {
        std::vector<int> distances;
        std::lock_guard<std::mutex> lock(treeMutex);

        getAllDistancesRec(root, distances);
        return distances;
    }

    void displayInstrumentMovements(int min_distance, int max_distance) {
        int totalMovements = sumInRange(min_distance, max_distance);

        std::cout << "Surgical Instrument Tracking System:\n";
        std::cout << "------------------------------------\n";
        std::cout << "Calculating total movements of instruments within range:\n";
        std::cout << "Minimum distance: " << min_distance << " mm\n";
        std::cout << "Maximum distance: " << max_distance << " mm\n";
        std::cout << "Total movements: " << totalMovements << " units\n";
        std::cout << "------------------------------------\n";
    }

};

int main() {
    SurgicalInstrumentTracker tracker;

    // Insert the example data
    std::vector<int> instrumentDistances = {100, 50, 150, 30, 70, 180};
    for (int distance : instrumentDistances) {
        tracker.insert(distance);
    }

    std::cout << "Surgical Instrument Tracking System\n";
    std::cout << "===================================\n";
    std::cout << "Instrument distances in the system (in mm):\n";
    for (int distance : tracker.getAllDistances()) {
        std::cout << distance << " ";
    }
    std::cout << "\n\n";

    int min_distance = 70;
    int max_distance = 150;

    tracker.displayInstrumentMovements(min_distance, max_distance);

    return 0;
}
