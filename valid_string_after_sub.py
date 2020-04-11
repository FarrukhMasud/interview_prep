class Solution:
    def isValid(self, S: str) -> bool:
        import re

        res = re.sub(r"abc", "", S)
        res = re.sub(r"abc", "", res)
        return not res or res == "abc"


tests = [
    ("aaabcbcbc", True),
    ("abc", True),
    ("aabcbc", True),
    ("abcabcababcc", True),
    ("abccba", False),
    ("cababc", False),
]
sol = Solution()
for test in tests:
    res = sol.isValid(test[0])
    if res == test[1]:
        print("Test passed:\t{}".format(test[0]))
    else:
        print("Test failed:\t{}\t\t{}".format(test[0], res))
