# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # while headA:
        #     temp = headB
        #     while temp:
        #         if temp is headA:
        #             return temp
        #         temp = temp.next
        #     headA = headA.next
        tempA, tempB = headA, headB
        countA = countB = 0
        while tempA:
            countA += 1
            tempA = tempA.next

        while tempB:
            countB += 1
            tempB = tempB.next
        while (countA > countB):
            countA -= 1
            headA = headA.next
        while (countB > countA):
            countB -= 1
            headB = headB.next
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
