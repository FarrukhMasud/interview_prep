class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(0, len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp[0])):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]


s = "aaa"
p = "ab*a*c*a"
result = Solution().isMatch(s, p)
print(result)
