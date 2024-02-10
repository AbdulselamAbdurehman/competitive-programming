# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode("dummy")
        dummy.next = head
    
        left, right = dummy, head
        while right:
            if right.val == val:
                left.next = right.next
            else:
                left = left.next
            right = right.next
        return dummy.next
