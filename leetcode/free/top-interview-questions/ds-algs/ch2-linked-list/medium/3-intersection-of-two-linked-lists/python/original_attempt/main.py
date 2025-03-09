
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode, skipA: int, skipB: int, intersectVal: int) -> ListNode:
        intersectionNode = None

        currentNodeA = headA
        currentNodeB = headB

        skipACount = 0
        while currentNodeA:
            if skipACount < skipA:
                currentNodeA = currentNodeA.next
                skipACount += 1
            else:
                if currentNodeA.val == intersectVal:
                    break
                else:
                    return None
            

        while currentNodeB:


def main():
    sol = Solution()

    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3

    intersectNode = sol.getIntersectionNode(listA, listB, skipA, skipB, intersectVal)

    print(intersectNode.val)

    # intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2

if __name__ == "__main__":
    main()
