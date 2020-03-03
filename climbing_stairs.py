class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        i = 1
        j = 0
        x = 0
        while x < n:
            x += 1
            temp = i
            i = i + j
            j = temp
            # print("{}\t{}".format(x, i))
        return i


i = 5
result = Solution().climbStairs(i)
print(result)

# 1 + 1
# 2


# 1 + 1 + 1
# 2 + 1
# 1 + 2


# 1 + 1 + 1 + 1
# 2 + 1 + 1
# 1 + 2 + 1
# 1 + 1 + 2
# 2 + 2

