class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""

        carry = 0
        result = ""
        while len(num1) > 0 or len(num2) > 0:
            x = int(num1[-1]) if len(num1) > 0 else 0
            y = int(num2[-1]) if len(num2) > 0 else 0
            sum1 = x + y + carry
            carry = int(sum1 / 10)
            sum1 = int(sum1 % 10)
            result = str(sum1) + result
            num1 = num1[0:-1]
            num2 = num2[0:-1]

        if carry > 0:
            result = str(carry) + result
        return result


n = "1"
m = "1000"
result = Solution().addStrings(n, m)
print(result)
