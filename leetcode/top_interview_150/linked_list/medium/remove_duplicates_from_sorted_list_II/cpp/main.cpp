#include <iostream>

/**
**Leetcode Problem:**

- https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

**ChatGPT solution:**

- https://chatgpt.com/share/66e783f0-9b74-8005-8550-12e839f0fed2

*/

/**
Approach: Remove duplicates from a sorted linked list in C++

Step 1: Create a dummy node to handle edge cases
    - dummy node is set to 0 and linked to the head of the list

Step 2: Traverse the list while checking for duplicates
    - if duplicates are found, skip them by linking the previous node to the next non-duplicate node
    - if no duplicates are found, move to the next node

Step 3: Once the traversal is complete, 
    - return the next node of the dummy node as the new head of the list

*/

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

/**
// Time Complexity: O(n)
    - where n is the number of nodes in the linked list
    - we traverse the list once to remove duplicates
// Space Complexity: O(1)
    - we only use a few extra pointers
*/
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // Create a dummy node to handle edge cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* current = head;

        while (current) {
            // If the current node has duplicates
            if (current->next && current->val == current->next->val) {
                // Move to the last duplicate node, skipping all duplicates
                while (current->next && current->val == current->next->val) {
                    current = current->next;
                }
                // Skip the duplicates, linking the previous node to the next non-duplicate node
                prev->next = current->next;
            } else {
                // Move to the next node when no duplicates are found
                prev = prev->next;
            }
            current = current->next;
        }

        return dummy->next;
    }
};

void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next->next = new ListNode(5);

    Solution solution;
    std::cout << "Original List: ";
    printList(head);

    std::cout << "List after Removing Duplicates: ";
    ListNode* result = solution.deleteDuplicates(head);
    printList(result);

    return 0;
}
