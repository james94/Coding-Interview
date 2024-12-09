#include <stdexcept>
#include <memory>
#include <concepts>



// Define a concept for numeric types
template<typename T>
concept Numeric = std::is_arithmetic_v<T>;

// Binary Tree Node structure
template <Numeric T>
struct TreeNode {
    T intensity;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;

    TreeNode(T val) : intensity(val), left(nullptr), right(nullptr) {}
};

// Function to sum intensities within range
template <Numeric T>
T sumIntensitiesInRange(const TreeNode<T>* root, T low, T high) {
    if (root == nullptr) {
        return 0;
    }

    // If current node's intensity is within range, include it in sum
    T sum = (root->intensity >= low && root->intensity <= high) ? root->intensity : 0;

    // If current node's intensity is greater than low, explore left subtree
    if (root->intensity > low) {
        sum += sumIntensitiesInRange(root->left.get(), low, high);
    }

    // If current node's intensity is less than high, explore right subtree
    if (root->intensity < high) {
        sum += sumIntensitiesInRange(root->right.get(), low, high);
    }

    return sum;
}

// Wrapper function for input validation and error handling
template<Numeric T>
T analyzeBrainRegions(const TreeNode<T>* root, T low, T high) {
    // Input validation
    if (low > high) {
        throw std::invalid_argument("Low threshold must be less than or equal to high threshold");
    }
    if (low < 1 || high > 1000) {
        throw std::out_of_range("Thresholds must be between 1 and 1000");
    }

    return sumIntensitiesInRange(root, low, high);
}
