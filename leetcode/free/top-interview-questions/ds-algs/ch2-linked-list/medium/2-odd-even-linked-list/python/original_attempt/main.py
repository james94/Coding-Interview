class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        odd = None
        even = None

        while current:
            if current.val % 2 == 0: # Even
                # I think might need to keep track of first even, so odd can point to it later
                if even is None: 
                    even = current
                else:
                    even = current.next
                # even = current.val
            else: # Odd
                if odd is None:
                    odd = current
                else:
                    odd = current.next
                # odd = current.val

            current = current.next


def main():
    head = [1,2,3,4,5]

    Solution soln
    soln.oddEvenList(head)
