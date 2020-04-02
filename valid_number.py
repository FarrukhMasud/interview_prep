class Solution:
    def isNumber(self, s: str) -> bool:
        import re

        s = s.strip()
        if not s:
            return False
        p = re.compile("\A(-|\+)?((\d+(\.\d*)?)|(\.\d+))(e(-|\+)?\d+)?\Z")
        result = p.match(s)
        return result is not None


tests = [
    ("0", True),
    (".1", True),
    (" 0.1 ", True),
    ("abc", False),
    ("1 a", False),
    ("2e10", True),
    (" -90e3   ", True),
    (" 1e", False),
    ("e3", False),
    (" 6e-1", True),
    (" 99e2.5 ", False),
    ("53.5e93", True),
    (" --6 ", False),
    ("-+3", False),
    ("95a54e53", False),
]
s = Solution()
for test in tests:
    r = s.isNumber(test[0])
    if r == test[1]:
        print("Test passed\t:" + test[0])
    else:
        print("Test failed\t:" + test[0])
