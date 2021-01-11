class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return 0

        max_depth = 0
        current_depth = 0
        for c in s:
            if c == "(":
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ")":
                current_depth -= 1
        return max_depth


inputs = [
    ("(1+(2*3)+((8)/4))+1", 3),
    ("(1)+((2))+(((3)))", 3),
    ("1+(2*3)/(2-1)", 1),
    ("", 0),
    ("1", 0),
]

sol = Solution()
for s in inputs:
    res = sol.maxDepth(s[0])
    if res != s[1]:
        print(
            "ERROR rescrived: {} while expecting {} for input {}".format(
                res, s[1], s[0]
            )
        )
    else:
        print("Test passed for {}".format(s[0]))
