class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = right = 0
        left_move = right_move = 0
        for i in range(len(boxes)-1, -1, -1):
            right_move += right
            if boxes[i] == "1":
                right += 1
        result = []
        for j in range(len(boxes)):
            result.append(right_move + left_move )
            if boxes[j] == "1":
                right -= 1
                left += 1
            left_move += left
            right_move -= right
        return result
