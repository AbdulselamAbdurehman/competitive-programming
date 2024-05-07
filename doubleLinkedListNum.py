# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        carry, tail = 0, None
        while stack:
            curr = stack.pop() * 2 + carry
            val, mod = divmod(curr, 10)
            carry, tail = val, ListNode(mod, tail)
        if carry:
            tail = ListNode(carry, tail)
        return tail
