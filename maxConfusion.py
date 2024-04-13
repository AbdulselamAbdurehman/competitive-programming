class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maxConsecutive(answerKey, k, 'T'), 
        self.maxConsecutive(answerKey, k, 'F'))

    def maxConsecutive(self, answerKey, k, ans):
        maximum = curr = i = 0
        for j in range(len(answerKey)):
            if answerKey[j] == ans:
                curr += 1
            while curr > k:
                if answerKey[i] == ans:
                    curr -= 1
                i += 1
            maximum = max(j-i+1, maximum)
        return maximum
