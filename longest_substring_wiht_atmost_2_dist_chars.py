class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s.strip()) == 0:
            return 0
        maxLength = 0
        currentString = []
        for i in s:
            currentString.append(i)
            temp = set(currentString)
            while len(temp) > 2:
                currentString.pop(0)
                temp = set(currentString)
            if len(currentString) > maxLength:
                maxLength = len(currentString)
        return maxLength


s = "abc"
result = Solution().lengthOfLongestSubstringTwoDistinct(s)
print(result)
