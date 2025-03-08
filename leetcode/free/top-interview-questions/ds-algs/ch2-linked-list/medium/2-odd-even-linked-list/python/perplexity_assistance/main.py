# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#13
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Linked List Manipulation: Rearranging nodes by adjusting pointers
# - Two-Pointer Technique: Separating the list into odd and even groups using pointers
#
# Clarifying Questions:
#
# 1. Are the node indices 1-based or 0-based?
#   - The problem states the first node is considered odd (1-based)
#
# 2. Can the input list be empty?
#   - Yes, but the constraints state 1 <= nodes <= 10^4, so we handle empty
#       lists gracefully
#
# Potential Solutions:
#
# 1. Brute Force: Collect nodes in two lists (odd and even) and merge them.
#   This uses O(n) space.
#
# 2. In-Place Pointer Manipulation: Use two pointers to split the list into
#   odd and even groups without extra space.
#
##
# While Coding
##
#
# Implementation we'll use O(1) space
#
# Explanation of Solution:
#
#   1. Initialization:
#       - odd starts at the first node (head)
#       - even starts at the second node (head.next)
#       - even_head saves the start of the even list for later merging.
#   2. Traversal:
#     - While even and even.next exist:
#       - Update odd.next to skip the next even node
#       - Move odd forward
#       - Update even.next to skip the next odd node.
#       - Move even forward
#   3. Merge:
#       - Link the end of the odd list (odd.next) to start of the even list (even_head)
#
##
# After Coding
##
#
# Potential Improvements:
#
#   - Time Complexity: O(n), as we traverse the list once.
#   - Space Complexity: O(1), using only a few pointers.
#   - Edge Cases:
#       - Single-node list: Returns the node as-is
#       - Two-node list: -> Output
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd = head          # Pointer for odd-indexed nodes
        even = head.next    # Pointer for even-indexed nodes
        even_head = even    # Save the start of the even list

        while even and even.next:
            # Link odd nodes
            odd.next = even.next
            odd = odd.next

            # Link even noes
            even.next = odd.next
            even = even.next
        
        # Merge the two lists
        odd.next = even_head
        return head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("->".join(res) if res else "Empty List")

def main():
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5) ) ) ) )
    sol = Solution()

    new_head1 = sol.oddEvenList(head1)
    print_list(new_head1)

    # Example 2
    head2 = ListNode(2)
    head2.next = ListNode(1)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(5)
    head2.next.next.next.next = ListNode(6)
    head2.next.next.next.next.next = ListNode(4)
    head2.next.next.next.next.next.next = ListNode(7)

    new_head2 = sol.oddEvenList(head2)
    print_list(new_head2)

if __name__ == "__main__":
    main()
