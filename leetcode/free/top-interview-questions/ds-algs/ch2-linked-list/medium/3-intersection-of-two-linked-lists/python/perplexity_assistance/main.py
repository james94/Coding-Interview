# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#20
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Linked Lists: Understanding the structure and traversal of linked lists.
# - Two-Pointer Technique: Using two pointers to traverse the lists efficiently
# - Floyd's Cycle-Finding Algorithm: Adapting this concept to find the intersection point.
#
# Clarifying Questions:
#
# 1. Can the lists have different lengths?
#   - Yes, the lists can have different lengths
#
# 2. Is the intersection based on node reference or value?
#   - The intersection is based on node reference, not just value
#
# 3. Can we modify the original list?
#   - No, the original structure of the lists must be preserved
#
# Potential Solutions:
#
# 1. Brute Force: Compare every node of listA with every node of listB (O(m*n) time, O(1) space)
#
# 2. Hash Set: Store all nodes of one list in a set, then check nodes of the other list (O(m+n) time, O(m) space)
#
# 3. Two-Pointer Technique: Traverse both lists, switch to the other list's head when reaching the end (O(m+n) time, O(1) space).
#
##
# While Coding
##
#
# Implementation we'll use Two-Pointer Technique
#
# Explanation of Solution:
#
# 1. Initialization: Start two pointers, ptrA and ptrB, at the heads of the respective lists.
#
# 2. Traversal:
#   - Move both pointers one step at a time
#   - When a pointer reaches the end of its list, redirect it to the head of the other list
#
# 3. Intersection Detection:
#   - If there's an intersection, both pointers will meet at the intersection node.
#   - If there's no intersection, both pointers will become None.
#
##
# After Coding
##
#
#   - Time Complexity: O(m+n), where m and n are the lengths of the two lists
#   - Space Complexity: O(1), as we only use two pointers regardless of list sizes
#
# Potential Improvements:
#
# 1. Early Termination:
#   - Check if the last nodes are the same before starting the main algorithm.
#   - If they're different, there's no intersection
#
# 2. Length Calculation:
#   - Calculate lengths of both lists first
#   - Move the pointer of the longer list ahead by the difference in lengths
#   - Then move both pointers together until they meet
#
# Edge Cases:
#
#   - One of both lists are empty
#   - Lists of significantly different lengths
#   - No intersection between the lists

# We use Two-Pointer Technique
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            # Move to the next node, or to the head of the other list if end is reached
            ptrA = ptrA.next if ptrA else headB

            ptrB = ptrB.next if ptrB else headA

        # This will be either the intersection point or None
        return ptrA

def main():
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
    
    # Test Case 1: Intersection Exists
    common = create_linked_list([8, 4, 5])
    headA = create_linked_list([4, 1])
    headA.next.next = common
    headB = create_linked_list([5, 6, 1])
    headB.next.next.next = common

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)
    print("Test 1 Result:", result.val if result else None) # Should print 8

    # Test Case 2: No Intersection 
    headA = create_linked_list([2, 6, 4])
    headB = create_linked_list([1, 5])
    result = sol.getIntersectionNode(headA, headB)
    print("Test 2 Result:", result.val if result else None) # Should print None

if __name__ == "__main__":
    main()
