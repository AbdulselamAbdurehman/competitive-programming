# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current, count = head, 0
        while current:
            count += 1
            current = current.next
        if n == count:
            return head.next
        pointer = head
        for i in range(1, count-n):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return head
