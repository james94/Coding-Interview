#include <iostream>
#include <optional>
#include <vector>
#include <queue>

struct TreeNode {
    int elevation;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : elevation(val), left(nullptr), right(nullptr) {}
};

class UASTerrainNavigation {
public:
    // calculate the sum of elevations within the given range
    static int sumElevationRange(TreeNode* root, int low, int high) {
        if (root == nullptr) {
            return 0;
        }

        // If current node's elevation is within range, include it and recurse both sides
        if (root->elevation >= low && root->elevation <= high) {
            return root->elevation +
                sumElevationRange(root->left, low, high) +
                sumElevationRange(root->right, low, high);
        }

        // If current elevation is less than low, only recurse right
        if (root->elevation < low) {
            return sumElevationRange(root->right, low, high);
        }

        // If current elevation is greater than high, only recurse left
        return sumElevationRange(root->left, low, high);
    }

    // Helper function to build the DEM tree from an array representation
    static TreeNode* buildDEMTree(const std::vector<std::optional<int>>& values) {
        if (values.empty() || !values[0].has_value()) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(values[0].value());
        std::queue<TreeNode*> queue;
        queue.push(root);

        for (size_t i = 1; i < values.size(); i += 2) {
            TreeNode* current = queue.front();
            queue.pop();

            if (i < values.size() && values[i].has_value()) {
                current->left = new TreeNode(values[i].value());
                queue.push(current->left);
            }

            if (i + 1 < values.size() && values[i + 1].has_value()) {
                current->right = new TreeNode(values[i + 1].value());
                queue.push(current->right);
            }
        }

        return root;
    }

    static void displayElevationSummary(const std::vector<std::optional<int>>& dem, int low, int high, int result) {
        std::cout << "UAS Terrain-Referenced Navigation System\n";
        std::cout << "----------------------------------------\n";
        std::cout << "Digital Elevation Model (DEM): ";
        for (const auto& val : dem) {
            if (val.has_value()) {
                std::cout << val.value() << " ";
            }
            else {
                std::cout << "null ";
            }
        }
        std::cout << "\nElevation range: [" << low << " m, " << high << " m]\n";
        std::cout << "Sum of elevations within range: " << result << " m\n";
        std::cout << "This data is crucial for terrain-following algorithms and obstacle avoidance.\n";
        std::cout << "---------------------------------------------------\n\n";
    }
};

int main() {
    // Example 1
    std::vector<std::optional<int>> dem1 = {100,50,150,30,70,std::nullopt,180};
    TreeNode* root1 = UASTerrainNavigation::buildDEMTree(dem1);
    int low1 = 70, high1 = 150;
    int result1 = UASTerrainNavigation::sumElevationRange(root1, low1, high1);
    // std::cout << "Example 1 Result: " << result1 << std::endl;
    UASTerrainNavigation::displayElevationSummary(dem1, low1, high1, result1);

    // Example 2
    std::vector<std::optional<int>> dem2 = {100,50,150,30,70,130,180,10,std::nullopt,60};
    TreeNode* root2 = UASTerrainNavigation::buildDEMTree(dem2);
    int low2 = 60, high2 = 100;
    int result2 = UASTerrainNavigation::sumElevationRange(root2, low2, high2);
    // std::cout << "Example 2 Result: " << result2 << std::endl;
    UASTerrainNavigation::displayElevationSummary(dem2, low2, high2, result2);

    return 0;
}
