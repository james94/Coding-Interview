#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

/**
 * Since we are traversing every n node in tree1,
 * we are also doing a traversal m in tree2
 * 
 * Time Complexity: O(n + m)
 * 
 * Since we are keeping a list of every n element
 * in tree1, we also are doing an inorder traversal m
 * on tree2
 * 
 * Space Complexity: O(n + m)
 * 
 * YouTube: Solving My Amazon Phone Interview
 * In video, solution was done in Java, but I
 * did my solution in the code below in C++.
 * https://www.youtube.com/watch?v=7lbwfkCfNQ4
 */


class TreeNode {
    public:
        int val;
        TreeNode *left;
        TreeNode *right;

    TreeNode(int val) {
        this->val = val;
    }
};

// Approach 1: inorder using recursion
// now we have a working solution
void inorder(TreeNode *root, vector<int> &list) {
    if(root == NULL) return;

    inorder(root->left, list);
    // cout << "root->val = " << root->val << endl;
    list.push_back(root->val);
    inorder(root->right, list);
}

// Approach 2: go into existing solution, optimize it
// Instead of creating a list for each tree. We will create
// a list for the first tree and as we do our traversal for
// the 2nd tree, we can do our check there to see if they
// have the same in order traversal

// function does check while going through inorder traversal
bool inorderCheck(TreeNode *root, vector<int> &list) {
    if(root == NULL) return true;

    // check on 1st recursive call, does it return false, if true, then return false
    if(inorderCheck(root->left, list) == false)
    {
        return false;
    }

    // check if value in our list equals current node we are on
    // if list is empty, we know we don't have a match
    // likewise, if list 1st element doesn't match current node value we are on, return false
    if(list.size() == 0 || list[0] != root->val)
    {
        return false;
    }

    // afterwards, remove that element since we no longer need to check it
    // cout << "root->val = " << root->val << endl;
    // cout << "list[0] = " << list[0] << endl;
    list.erase(list.begin());

    // likewise, on right subtree, we see does it return true or false
    return inorderCheck(root->right, list);
}

int main()
{
    TreeNode *tree1 = new TreeNode(5);
    tree1->left = new TreeNode(3);
    tree1->left->left = new TreeNode(1);
    tree1->right = new TreeNode(7);
    // comment out node right left in tree to make tree1 different from tree2
    tree1->right->left = new TreeNode(6);

    TreeNode *tree2 = new TreeNode(3);
    tree2->left = new TreeNode(1);
    tree2->right = new TreeNode(6);
    tree2->right->left = new TreeNode(5);
    // comment out right right node 7 in tree when switching it with 8 
    tree2->right->right = new TreeNode(7);
    // change node right right node in tree to make tree2 different from tree1
    // tree2->right->right = new TreeNode(8);

    vector<int> list1;
    // vector<int> list2; // we longer need list2 with inorderCheck
    cout << "inorder tree1:" << endl;
    inorder(tree1, list1);

    // commented out inorder to create 2nd list from tree2 since we 
    // are using inorderCheck
    // cout << "inorder tree2:" << endl;
    // inorder(tree2, list2);
    
    // cout << "list1: ";
    // for(int i = 0; i < list1.size(); i++)
    // {
    //     cout << list1[i] << ", ";
    // }

    // cout << endl;

    // cout << "list2: ";
    // for(int i = 0; i < list2.size(); i++)
    // {
    //     cout << list2[i] << ", ";
    // }

    // cout << endl;

    // if(list1 == list2)
    // {
    //     cout << "same in order traversal" << endl;
    // }
    // else
    // {
    //     cout << "different in order traversal" << endl;
    // }

    // optimize with inorderCheck
    cout << "optimize with inorderCheck tree2 == list1?:" << endl;
    bool same_traversal = inorderCheck(tree2, list1);
    // both binary trees have same inorder traversal and list1 is size 0
    if(same_traversal && list1.size() == 0)
    {
        cout << "both binary trees HAVE same inorder traversal" << endl;
    }
    else
    {
        cout << "both binary trees DON'T have same inorder traversal" << endl;
    }
    return 0;
}