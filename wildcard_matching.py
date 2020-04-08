class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        px = []
        for i, c in enumerate(p):
            if i < len(p) - 1 and c == "*" and p[i + 1] == "*":
                continue
            px.append(c)
        p = "".join(px)
        if not p:
            return False
        if p == "*":
            return True
        dp = [[False] * (len(p) + 1) for _ in range(0, len(s) + 1)]
        dp[0][0] = True
        dp[0][1] = p[0] == "*"

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]


s = "adceb"
p = "*a*b"
result = Solution().isMatch(s, p)
print(result)
