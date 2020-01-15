class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            x = 1 if i >= 0 and a[i] == "1" else 0
            y = 1 if j >= 0 and b[j] == "1" else 0
            r = x + y + carry
            if r % 2 == 0:
                result = "0" + result
            else:
                result = "1" + result
            if r > 1:
                carry = 1
            else:
                carry = 0
            i = i - 1
            j = j - 1
        if carry > 0:
            result = "1" + result
        return result


a = "10"
b = "1010"

sol = Solution()
r = sol.addBinary(a, b)
print(r)
