#include <iostream>
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
    std::unique_ptr<TreeNode> left;
    std::unique_ptr<TreeNode> right;

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

// Helper function to create a sample binary tree
template<Numeric T>
std::unique_ptr<TreeNode<T>> createSampleTree() {
    auto root = std::make_unique<TreeNode<T>>(100);
    root->left = std::make_unique<TreeNode<T>>(50);
    root->right = std::make_unique<TreeNode<T>>(150);
    root->left->left = std::make_unique<TreeNode<T>>(30);
    root->left->right = std::make_unique<TreeNode<T>>(70);
    root->right->right = std::make_unique<TreeNode<T>>(180);
    return root;
}

template<Numeric T>
void displayContextResult(const TreeNode<T>* root, int low, int high) {
    std::cout << "Medical Imaging Software for Brain MRI Analysis:\n";
    std::cout << "------------------------------------------------\n";
    std::cout << "Analyzing brain regions using hierarchical segmentation...\n\n";

    try {
        int result = analyzeBrainRegions(root, low, high);
        std::cout << "Analysis Results:\n";
        std::cout << "- Intensity range of interest: [" << low << ", " << high << "]\n";
        std::cout << "- Sum of average intensities for regions within range: " << result << "\n";
        std::cout << "\nInterpretation: The total intensity of " << result
                  << " represents the cumulative signal strength of brain regions\n"
                  << "with average pixel intensities between " << low << " and " << high << ".\n";
        std::cout << "This quantification helps identify and measure regions of interest in the brain MRI.\n";
    } catch (const std::exception& e) {
        std::cerr << "Error in analysis: " << e.what() << std::endl;
    }
}

int main() {
    auto root = createSampleTree<int>();
    int low = 70, high = 150;

    displayContextResult<int>(root.get(), low, high);


    return 0;
}