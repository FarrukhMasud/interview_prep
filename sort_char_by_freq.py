from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        x = dict()
        for c in s:
            if c in x:
                x[c] = x[c] + 1
            else:
                x[c] = 1
        lst = [i * x[i] for i in x]
        lst1 = sorted(lst, key=lambda z: len(z), reverse=True)
        return "".join(lst1)


sol = Solution()
result = sol.frequencySort("loveleetcode")
print(result)
