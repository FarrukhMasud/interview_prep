from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            t = s[left]
            s[left] = s[right]
            s[right] = t
            left += 1
            right -= 1

