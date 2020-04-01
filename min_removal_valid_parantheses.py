class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stck = []
        rs = []
        for i, c in enumerate(s):
            if c == "(":
                stck.append((c, i))
            elif c == ")":
                if stck:
                    stck.pop()
                else:
                    rs.append((c, i))
        if not stck and not rs:
            return s
        stck.extend(rs)
        stck = sorted(stck, key=lambda x: x[1])

        result = []
        for i, c in enumerate(s):
            if stck and stck[0][1] == i:
                stck.pop(0)
            else:
                result.append(c)

        return "".join(result)


s = "(a(b(c)d)"
result = Solution().minRemoveToMakeValid(s)
print(result)
