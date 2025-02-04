#
"""
Ex1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list_result = ListNode()
        temp_l1_node = l1
        temp_l2_node = l2
        while temp_l1_node and temp_l2_node:
            print(f"l1 node = {temp_l1_node.val}")
            print(f"l2 node = {temp_l2_node.val}")
            list_result.val = temp_l1_node.val + temp_l2_node.val
            print(f"Added l1 and l2 nodes = {list_result.val}")
            temp_l1_node = temp_l1_node.next
            temp_l2_node = temp_l2_node.next
            list_result.next = ListNode()
        return list_result

def main():
    # l1 = [2,4,3], l2 = [5,6,4]
    # My implementation didn't account for when we pass 0 to 9, for instance 4+6 = 10
    # and so, we reverse l1 and l2, then add them together, that 10 would keep 0, then carry
    # 1 over to left integer and add 1 along with 3 and 4
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

if __name__ == "__main__":
    main()
