# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        linked_list = []
        current = head
        while current:
            linked_list.append(ListNode(current.val))
            current = current.next
        sorted_linked = sorted(linked_list, key=lambda item: item.val)
        for i in range(len(sorted_linked)-1):
            sorted_linked[i].next = sorted_linked[i+1]
        return sorted_linked[0]
        
