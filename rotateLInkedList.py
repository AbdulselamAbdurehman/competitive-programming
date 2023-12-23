
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        curr = head
        count = 1
        while ( curr.next ):
            curr = curr.next
            count += 1

        k = k % count            
        curr.next = head
        temp = head
        for _ in range(count - k - 1):
            temp = temp.next
        
        new_node = temp.next
        temp.next = None
        return new_node
