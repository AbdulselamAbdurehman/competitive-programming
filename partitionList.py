# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = less = None
        current = head
        while current:
            if current.val < x:
                if not less:
                    less = ListNode(current.val)
                    left = less
                else:
                    less.next = ListNode(current.val)
                    less = less.next
            current = current.next
        if not left:
            return head
        while head:
            if head.val >= x:
                less.next = head
                less = less.next
            head = head.next
        less.next = None
        return left
