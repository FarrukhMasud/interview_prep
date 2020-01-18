class Solution:
    def firstUniqChar(self, str: str) -> int:
        unique = set()
        non_unique = set()
        for s in str:
            if s in non_unique:
                continue
            if s in unique:
                unique.remove(s)
                non_unique.add(s)
            else:
                unique.add(s)
        for i, s in enumerate(str):
            if s in unique:
                return i

        return -1


sol = Solution()
res = sol.firstUniqChar("leetcode")
print(res)
