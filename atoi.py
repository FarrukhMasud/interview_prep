class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or len(s) == 0 or not s.strip():
            return 0
        s = s.strip()
        sign = False
        if s[0] == "-" or s[0] == "+":
            sign = s[0] == "-"
            s = s[1:]

        result = 0
        coeff = 10
        for c in s:
            if not c.isdigit():
                break
            result = (result * coeff) + int(c)
            # coeff = coeff * 10
        result = result if not sign else result * -1
        if result < -2147483648:
            return -2147483648
        if result >= 2147483647:

            return 2147483647
        return result


sol = Solution()
x = sol.myAtoi("-420 ifdsfs ")
print(x)

