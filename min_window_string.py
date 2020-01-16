# This would only work if the t have unique characters


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        map = dict()
        for i in t:
            map[i] = -1
        result = " " * len(s)
        for i, c in enumerate(s):
            if c in map:
                map[c] = i
                flag = False
                m1 = 100000000
                m2 = -10000
                for j in map:
                    if map[j] < 0:
                        flag = True
                        break
                    m1 = min(m1, map[j])
                    m2 = max(m2, map[j])
                if flag:
                    continue
                temp = s[m1 : m2 + 1]
                if len(temp) <= len(result):
                    result = temp

        return result.strip()


# s = "ADOBECODEBANC"
# t = "ABC"
s = "abc"
t = "ac"
sol = Solution()
result = sol.minWindow(s, t)
print(result)
