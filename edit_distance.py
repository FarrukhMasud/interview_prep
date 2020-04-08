class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if not word1 or not word2:
            return 0

        dp = [[0] * (len(word1) + 1) for _ in range(0, len(word2) + 1)]
        for i in range(0, len(word1) + 1):
            dp[0][i] = i
        for i in range(0, len(word2) + 1):
            dp[i][0] = i

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = min(dp[i - 1][j], dp[i - i][j - 1], dp[i][j - 1])
                if word1[j - 1] != word2[i - 1]:
                    dp[i][j] += 1

        return dp[len(word2)][len(word1)]


word1 = "horse"
word2 = "ros"
result = Solution().minDistance(word1, word2)
print(result)
