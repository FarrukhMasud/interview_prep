class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i, _ in enumerate(s):
            x_result = self._longestPalindrome(s, i, i + 1, "")
            if len(x_result) > len(result):
                result = x_result
            x_result = self._longestPalindrome(s, i, i, "")
            if len(x_result) > len(result):
                result = x_result
        return result

    def _longestPalindrome(self, s: str, index: int, index1: int, mid_str: str) -> str:
        result = ""
        if index >= 0 and index1 < len(s):
            if s[index] == s[index1]:
                if index == index1:
                    result = s[index]
                else:
                    result = s[index] + mid_str + s[index1]
                x_result = self._longestPalindrome(s, index - 1, index1 + 1, result)
                if len(x_result) > 0:
                    result = x_result

        return result


sol = Solution()
x = sol.longestPalindrome("aabaa")
print(x)
