# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode((l1.val + l2.val) % 10)
        current = root
        rem = (l1.val + l2.val) // 10
        while not (l1.next == l2.next == None):
            if l1.next != None and l2.next != None:
                l1 = l1.next
                l2 = l2.next
                element = ListNode((l1.val + l2.val + rem) % 10)
                rem = (l1.val + l2.val + rem) // 10
            elif l1.next != None:
                l1 = l1.next
                element = ListNode((l1.val + rem) % 10)
                rem = (l1.val + rem) // 10
            else:
                l2 = l2.next
                element = ListNode((l2.val + rem) % 10)
                rem = (l2.val + rem) // 10
            current.next = element
            current = current.next
        if rem > 0:
            current.next = ListNode(rem)
        return root
