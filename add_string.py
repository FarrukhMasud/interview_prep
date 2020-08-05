class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""

        carry = 0
        result = ""
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            sum1 = x + y + carry
            carry = int(sum1 / 10)
            sum1 = int(sum1 % 10)
            result = str(sum1) + result
            i -= 1
            j -= 1

        if carry > 0:
            result = str(carry) + result
        return result


n = "12345"
m = "1000"
result = Solution().addStrings(n, m)
print(result)
