class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or len(s.strip()) == 0:
            return 0
        maxLength = 0
        currentString = []
        for i in s:
            currentString.append(i)
            temp = set(currentString)
            while len(temp) > k:
                currentString.pop(0)
                temp = set(currentString)
            if len(currentString) > maxLength:
                maxLength = len(currentString)
        return maxLength
