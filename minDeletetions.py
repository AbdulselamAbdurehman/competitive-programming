class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count, b_count = s.count('a'), 0
        result = math.inf
        for letter in s:
            if letter == 'a':
                a_count -= 1
            result = min(result, a_count + b_count)
            if letter == 'b':
                b_count += 1

        return result
