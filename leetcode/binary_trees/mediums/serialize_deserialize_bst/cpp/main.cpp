#include <iostream>
#include <climits>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

/*
**Leetcode Binary Tree Questions**:

- https://leetcode.com/problem-list/binary-tree/

**Leetcode Problem:**

- https://leetcode.com/problems/serialize-and-deserialize-bst/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM

**ChatGPT Solution:**

- https://chatgpt.com/share/67031379-b4a4-8005-85da-8643daac83ff
*/

/*
Software Design Perspective:

Serialization and deserialization of BST are crucial for storing and
transmitting tree data structures efficiently.

Full Stack Use Case in Robotics:

In a robotics system, a BST could be used to represent a robot's knowledge of
its environment or tasks.

Approach:

- Serialization: convert the tree into a string representation using pre-order
traversal. Pre-order traversal naturally works well with BST because the root
is processed before the subtrees, preserving the BST property.

- Deserialization: Reconstruct the BST from the serialized string by recursively
building it back using the BST property (left subtree contains smaller elements,
and right subtree contains larger elements)

Time Complexity:

- Serialization: O(n) where n is the number of nodes, as we visit
each node once during the pre-order traversal.

- Deserialization: O(n) since we are reconstructing the tree with
one pass through the serialized string.

Space Complexity:

- Serialization: O(n) for storing the serialized string.

- Deserialization: O(n) for storing the reconstructed tree
and the recursion stack in the worst case.

*/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Codec {
public:
    // Helper function to serialize the tree using pre-order traversal
    string serialize(TreeNode* root) {
        string result;
        serializeHelper(root, result);
        return result;
    }

    // Helper function to deserialize the tree using the serialized data.
    TreeNode* deserialize(string data) {
        if (data.empty()) {
            return nullptr;
        }

        stringstream ss(data);
        vector<int> values;
        string token;

        while (std::getline(ss, token, ',')) {
            values.push_back(stoi(token));
        }

        int index = 0;
        return deserializeHelper(values, index, INT_MIN, INT_MAX);

    }

private:

    // Recursive function for pre-order serialization
    void serializeHelper(TreeNode* root, string& result) {
        if (!root) {
            return;
        }

        result += to_string(root->val) + ",";
        serializeHelper(root->left, result);
        serializeHelper(root->right, result);
    }

    // Recursive function for deserialization
    TreeNode* deserializeHelper(const vector<int>& values, int& index, int minValue, int maxValue) {
        if (index >= values.size() || values[index] < minValue || values[index] > maxValue) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(values[index++]);
        root->left = deserializeHelper(values, index, minValue, root->val);
        root->right = deserializeHelper(values, index, root->val, maxValue);
        return root;
    }
};

// Helper function to print tree in pre-order fashion for testing
void printPreOrder(TreeNode* root) {
    if (!root) {
        return;
    }

    cout << root->val << " ";
    printPreOrder(root->left);
    printPreOrder(root->right);
}

int main() {

    Codec codec;

    // Example 1
    TreeNode* root1 = new TreeNode(2);
    root1->left = new TreeNode(1);
    root1->right = new TreeNode(3);
    string serialized1 = codec.serialize(root1);
    cout << "Serialized tree 1: " << serialized1 << endl;
    TreeNode* deserialized1 = codec.deserialize(serialized1);
    cout << "Deserialized PreOrder: ";
    printPreOrder(deserialized1);
    cout << endl;

    // Example 2
    TreeNode* root2 = nullptr;
    string serialized2 = codec.serialize(root2);
    cout << "Serialized tree 2: " << serialized2 << endl;
    TreeNode* deserialized2 = codec.deserialize(serialized2);
    cout << "Deserialized PreOrder: ";
    printPreOrder(deserialized2);
    cout << endl;

    return 0;
}