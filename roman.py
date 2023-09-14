def roman_to_arabic(roman: str) -> int:
        conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special = ("IV", "IX", "XL", "XC", "CD", "CM")
        index = num = 0
        while index < len(roman):
            if roman[index: index+2] in special:
                num = num + conversion[roman[index+1]] - conversion[roman[index]]
                index +=2
            else:
                num += conversion[roman[index]]
                index += 1
        return num
