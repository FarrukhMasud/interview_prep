class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        words = [
            ["I", "IV", "V", "IX"],
            ["X", "XL", "L", "XC"],
            ["C", "CD", "D", "CM"],
            ["M"],
        ]
        exp = 10
        index = 0
        while num > 0:
            c = int(num % exp)
            if c > 0:
                if c < 4:
                    result = (words[index][0] * c) + result
                elif c == 4:
                    result = words[index][1] + result
                elif c == 9:
                    result = words[index][3] + result
                else:
                    result = words[index][2] + (words[index][0] * (c - 5)) + result
            num = num / exp
            index = index + 1
        return result


num = 58
sol = Solution()
result = sol.intToRoman(num)
print(result)
