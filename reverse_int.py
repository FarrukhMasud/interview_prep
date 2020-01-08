class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        isneg = False
        if x < 0:
            isneg = True
            x = x * -1
        while x != 0:
            result = (result * 10) + int(x % 10)
            x = int(x / 10)
        if isneg:
            result = result * -1
        if result > 2147483647 or result < (2147483648 * -1):
            return 0
        return result


sol = Solution()
x = sol.reverse(-214)
print(x)
