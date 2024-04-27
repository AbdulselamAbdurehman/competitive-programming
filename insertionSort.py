# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curr = head

        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            coming = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = coming

        return dummy.next
