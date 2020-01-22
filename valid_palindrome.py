class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self._validPalidrome(s, 0, len(s) - 1, False)

    def _validPalidrome(
        self, s: str, left: int, right: int, hasAlredySeenDifferent: bool
    ):
        if left >= right:
            return True
        if s[left] == s[right]:
            return self._validPalidrome(s, left + 1, right - 1, hasAlredySeenDifferent)
        else:
            if hasAlredySeenDifferent:
                return False
            return self._validPalidrome(
                s, left + 1, right, True
            ) or self._validPalidrome(s, left, right - 1, True)


str = "abba"
sol = Solution()
result = sol.validPalindrome(str)
print(result)
