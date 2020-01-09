from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        prefix = ""
        i = 0
        while True:
            c = None
            for l in strs:
                if i >= len(l):
                    return prefix
                if c == None:
                    c = l[i]
                elif l[i] != c:
                    return prefix
            prefix = prefix + c
            i = i + 1

        return prefix


sol = Solution()
x = sol.longestCommonPrefix(["dog", "racecar", "car"])
print(x)
