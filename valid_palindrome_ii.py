class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = [
            c
            for c in s
            if (c >= "A" and c <= "Z")
            or (c >= "a" and c <= "z")
            or (c >= "0" and c <= "9")
        ]
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left = left + 1
            right = right - 1
        return True


str = "race a car"
sol = Solution()
result = sol.isPalindrome(str)
print(result)
