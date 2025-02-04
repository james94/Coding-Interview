# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#2
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

###
# Explanation:
###
#
# Linked List Iteration: through both linked lists simultaneously
#
# Digit Addition with Carry: It adds corresponding digits from both lists along
# with any carry from the previous iteration
#
# Result Construction: A new linked list is constructed with the sum of digits,
# handling carry for the next iteration

# Time Complexity: O(max(m, n)) where "m" and "n" are the lengths of the input linked lists
# Space Complexity: O(max(m, n)) for storing the result linked list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node for the result linked list
        dummy = ListNode(0)
        current = dummy

        # Initialize carry
        carry = 0

        # Iterate through both linked lists
        while l1 or l2:
            # Calculate the sum or current nodes and carry
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            # Update carry and create a new node with the digit value
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next

        # Handle remaining carry if any
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next

    def printList(self, linked_list):
        current = linked_list
        while current:
            print(current.val, end = " ")
            current = current.next

    def printReverse(self, list_node):
        if list_node is None:
            return
        
        # anything before recursive call will be done in order
        self.printReverse(list_node.next)
        # return after all recursive calls, then unwind backwards in reverse
        print(list_node.val, end = " ")


def main():
    # l1 = [2,4,3], l2 = [5,6,4]
    l1 = ListNode()
    l1.val = 2
    l1.next = ListNode()
    l1.next.val = 4
    l1.next.next = ListNode()
    l1.next.next.val = 3

    l2 = ListNode()
    l2.val = 5
    l2.next = ListNode()
    l2.next.val = 6
    l2.next.next = ListNode()
    l2.next.next.val = 4

    soln = Solution()
    list_result = soln.addTwoNumbers(l1, l2)
    # soln.printList(list_result)

    # print linked list in reverse using recursion
    soln.printReverse(list_result)

if __name__ == "__main__":
    main()
