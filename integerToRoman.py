class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        equivalents = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i, roman = 0, ""
        while num > 0:
            if num >= integers[i]:
                roman += equivalents[i]
                num -= integers[i]
            else:
                i += 1 
        return roman
