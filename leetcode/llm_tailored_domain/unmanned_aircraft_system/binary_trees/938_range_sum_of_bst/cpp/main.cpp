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
};

int main() {
    // Example 1
    std::vector<std::optional<int>> dem1 = {100,50,150,30,70,std::nullopt,180};
    TreeNode* root1 = UASTerrainNavigation::buildDEMTree(dem1);
    int result1 = UASTerrainNavigation::sumElevationRange(root1, 70, 150);
    std::cout << "Example 1 Result: " << result1 << std::endl;

    // Example 2
    std::vector<std::optional<int>> dem2 = {100,50,150,30,70,130,180,10,std::nullopt,60};
    TreeNode* root2 = UASTerrainNavigation::buildDEMTree(dem1);
    int result2 = UASTerrainNavigation::sumElevationRange(root1, 60, 100);
    std::cout << "Example 2 Result: " << result2 << std::endl;

    return 0;
}
