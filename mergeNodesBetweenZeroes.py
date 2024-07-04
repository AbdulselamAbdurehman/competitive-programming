# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast:
            merged_val = 0
            while fast.val != 0:
                merged_val += fast.val
                fast = fast.next
            slow.val = merged_val
            slow.next = fast.next
            slow = slow.next
            fast = fast.next
        return head
