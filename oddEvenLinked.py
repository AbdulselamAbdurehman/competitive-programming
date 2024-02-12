# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(-1)
        even_head = ListNode(-1)
        odd, even = odd_head, even_head
        index = 1
        while head:
            if index == 1:
                odd.next = head
                odd, index = head, 0
            else:
                even.next = head
                even, index = head, 1
            head = head.next
        even.next = None
        odd.next = even_head.next
        return odd_head.next
