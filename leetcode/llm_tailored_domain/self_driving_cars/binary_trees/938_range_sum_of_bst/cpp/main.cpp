#include <iostream>
#include <stdexcept>
#include <mutex>
#include <iomanip>

struct DecisionNode {
    int safety_score;
    DecisionNode* left;
    DecisionNode* right;
    DecisionNode(int score) : safety_score(score), left(nullptr), right(nullptr) {}
};

class SelfDrivingCarSafetyScoreTracker {
private:
    std::mutex mtx;

    int calculateSafetyScoreHelper(DecisionNode* root, int min_threshold, int max_threshold) {
        if (root == nullptr) {
            return 0;
        }

        int sum = 0;
        if (root->safety_score >= min_threshold && root->safety_score <= max_threshold) {
            sum += root->safety_score;
        }

        if (root->safety_score > min_threshold) {
            sum += calculateSafetyScoreHelper(root->left, min_threshold, max_threshold);
        }
        if (root->safety_score < max_threshold) {
            sum += calculateSafetyScoreHelper(root->right, min_threshold, max_threshold);
        }

        return sum;
    }

public:
    int calculateSafetyScore(DecisionNode* root, int min_threshold, int max_threshold) {
        if (min_threshold > max_threshold) {
            throw std::invalid_argument("min_threshold must be less than or equal to max_threshold");
        }

        std::lock_guard<std::mutex> lock(mtx);
        return calculateSafetyScoreHelper(root, min_threshold, max_threshold);
    }

    void displaySafetyScoreResult(int result, int min_threshold, int max_threshold) {
        std::cout << std::setfill('=') << std::setw(50) << "=" << std::endl;
        std::cout << "Self-Driving Car Safety Score Tracker" << std::endl;
        std::cout << std::setfill('=') << std::setw(50) << "=" << std::endl;
        std::cout << "Given a binary tree representing a hierarchical" << std::endl;
        std::cout << "decision-making system for a self-driving car:" << std::endl;
        std::cout << std::endl;
        std::cout << "Total safety score for actions within the range" << std::endl;
        std::cout << "[" << min_threshold << "," << max_threshold << "]: " << result << std::endl;
        std::cout << std::setfill('=') << std::setw(50) << "=" << std::endl;
    }
};

int main() {
    DecisionNode* root = new DecisionNode(10);
    root->left = new DecisionNode(5);
    root->right = new DecisionNode(15);
    root->left->left = new DecisionNode(3);
    root->left->right = new DecisionNode(7);
    root->right->right = new DecisionNode(18);

    int min_threshold = 7;
    int max_threshold = 15;

    SelfDrivingCarSafetyScoreTracker sdc_safety_calculator;
    int result = sdc_safety_calculator.calculateSafetyScore(root, min_threshold, max_threshold);

    sdc_safety_calculator.displaySafetyScoreResult(result, min_threshold, max_threshold);

    delete root->right->right;
    delete root->left->right;
    delete root->left->left;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
