class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discount, stack = [0]*n, []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                discount[stack.pop()] = prices[i]
            stack.append(i)
        answer = [0]*n
        for i in range(n):
            answer[i] = prices[i] - discount[i]
        return answer 
