# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            left = temp.next
            right = left.next
            left.next = right.next
            right.next = left
            temp.next = right
            temp = left
        return dummy.next
