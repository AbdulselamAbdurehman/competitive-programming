class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        indices = sorted(range(n), key=lambda i: ratings[i]) #sort indices
        output = [0]*n # giveaways
        for index in indices:
            curr = 1
            if index > 0 and ratings[index] > ratings[index-1]:
                curr = output[index -1] + 1
            if index < n-1 and ratings[index] > ratings[index+1]:
                curr = max(curr, output[index+1] + 1)
            output[index] = curr
        return sum(output)
