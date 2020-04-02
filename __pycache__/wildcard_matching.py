class Solution:
    def __init__(self):
        super().__init__()
        self.cache = set()

    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not s and p == "*":
            return True
        if not s or not p:
            return False
        import re

        p = re.sub("\\*+", "*", p)
        return self._isMatch(s, 0, p, 0)

    def _isMatch(self, s, si, p, pi):
        if si >= len(s) and pi >= len(p):
            return True

        if si >= len(s) and p[pi:] == "*":
            return True

        if si >= len(s) or pi >= len(p):
            return False
        if "--" + s[si:] + "==" + p[pi] in self.cache:
            return False
        if p[pi] == "?":
            return self._isMatch(s, si + 1, p, pi + 1)
        elif p[pi] == "*":
            x1 = self._isMatch(s, si + 1, p, pi + 1)
            if x1:
                return True
            self.cache.add("--" + s[si + 1 :] + "==" + p[pi + 1 :])
            x2 = self._isMatch(s, si, p, pi + 1)
            if x2:
                return True
            self.cache.add("--" + s[si:] + "==" + p[pi + 1 :])
            x3 = self._isMatch(s, si + 1, p, pi)
            if x3:
                return True
            self.cache.add("--" + s[si + 1 :] + "==" + p[pi:])
        else:
            if s[si] != p[pi]:
                self.cache.add("==" + s + "--" + p)
                return False
            else:
                return self._isMatch(s, si + 1, p, pi + 1)


i = "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab"
p = "b*b*ab**ba*b**b***bba"


result = Solution().isMatch(i, p)
print(result)
