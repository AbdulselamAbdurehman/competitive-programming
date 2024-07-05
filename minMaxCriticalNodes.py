# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        """
        [minDistance, maxDistance]
        """
        result = [math.inf, -math.inf]
        first_critical = recent_critical = -1
        while head and head.next and head.next.next:
            curr = head.next
            coming = curr.next
            if first_critical > -1:
                first_critical += 1
                recent_critical += 1

            if min(head.val, coming.val) > curr.val or max(head.val, coming.val) < curr.val:

                if first_critical == -1:
                    first_critical += 1
                else:
                    result[0] = min(recent_critical, result[0])
                    result[1] = max(first_critical, result[1])

                recent_critical = 0

            head = head.next
        if result[0] == math.inf or result[1] == -math.inf:
            return [-1, -1]
        return result
