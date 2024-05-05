# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, curr = 0, head #To count the nodes in LL
        while curr:
            curr = curr.next
            n += 1
        result = []
        share, rem = divmod(n, k)
        for i in range(k):
            dummy = ListNode()
            curr = dummy
            for j in range(share):
                curr.next = head
                head, curr = head.next, curr.next
                curr.next = None
            if rem > 0:
                curr.next = head
                head, curr = head.next, curr.next
                curr.next = None
                rem -= 1
            result.append(dummy.next)
        return result
