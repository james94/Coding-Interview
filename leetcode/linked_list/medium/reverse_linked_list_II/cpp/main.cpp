#include <iostream>
/**
Approach: Reverse a linked list from position left to right
in one pass in C++

Initial Checks: if head is nullptr or left == right, return head
    - no changes are needed

Traversal to left-1 node: we will find the node before the left position,
    - which we will call prev

Reversing the sublist: we will reverse the nodes between left and right
    - this involves using three pointers: prev, curr, and next

Reattaching the reversed part: after reversing, we connect the reversed sublist
    - back to the original list

Return the new head: we return the modified list head

**Leetcode Problem:**

- https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

**ChatGPT solution:**

- https://chatgpt.com/share/66e77d9d-0c50-8005-b015-74655772a4dd
*/

// Definition for singly-linked list.
// Dummy Node: added before head to handle edge cases
// Two Pointers: prev is used to reac just before left node, start node at position left to be reversed
// Reverse Logic: iteratively reverse the sublist in-place adjusting pointers
// Time Complexity: O(n)
    // where n is the number of nodes in the linked list, making one pass through the list
// Space Complexity: O(1)
    // we only use a few extra pointers
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) {
            return head;
        }

        // Create a dummy node to handle edge cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;

        // Move `prev` to the node before the left position
        for (int i = 1; i < left; i++) {
            prev = prev->next;
        }

        // `start` is the first node of the sublist to be reversed
        ListNode* start = prev->next;
        ListNode* curr = start->next;

        // Reverse the sublist from `left` to `right`
            // NOTE: come back and review with a diagram
        for (int i = left; i < right; i++) {
            start->next = curr->next;
            curr->next = prev->next;
            prev->next = curr;
            curr = start->next;
        }

        // Return the new head; modified list
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
    // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    Solution solution;
    int left = 2, right = 4;
    std::cout << "Original List: ";
    printList(head);

    ListNode* newHead = solution.reverseBetween(head, left, right);
    std::cout << "Reversed List: ";
    printList(newHead);

    return 0;
}
