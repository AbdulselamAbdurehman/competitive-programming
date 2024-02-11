# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        left, right = dummy, head
        while right and right.next:
            if right.val == right.next.val:
                duplicate = right.val
                while right and right.val == duplicate:
                    right = right.next
                left.next = right
            else:
                right = right.next
                left = left.next
        return dummy.next
