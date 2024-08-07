class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        numeric = {
            0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }

        def helper(n):
            if n < 20:
                return numeric[n]
            if n < 100:
                return numeric[(n // 10)*10] + (" " + helper(n % 10) if n % 10 != 0 else "")
            if n < 1000:
                return helper(n // 100) + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
            if n < 1000000:
                return helper(n // 1000) + " Thousand" + (" " + helper(n % 1000) if n % 1000 != 0 else "")
            if n < 1000000000:
                return helper(n // 1000000) + " Million" + (" " + helper(n % 1000000) if n % 1000000 != 0 else "")
            return helper(n // 1000000000) + " Billion" + (" " + helper(n % 1000000000) if n % 1000000000 != 0 else "")
        
        return helper(num).strip()
