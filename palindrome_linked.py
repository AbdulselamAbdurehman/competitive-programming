# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        coming, n = None, 0
        while temp:
            curr = ListNode(temp.val)
            curr.next = coming
            coming = curr
            temp = temp.next
            n += 1
        for j in range(n):
            if head.val != curr.val:
                return False
            head, curr = head.next, curr.next 
        return True
        
