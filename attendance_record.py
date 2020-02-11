# easy question in leetcode
class Solution:
    def checkRecord(self, s: str) -> bool:
        if not s:
            return True
        if len(s) == 1:
            return True

        a_count = 0
        l_count = 0
        for c in s:
            if c == "A":
                if a_count >= 1:
                    return False
                else:
                    a_count = 1

            if c == "L":
                if l_count >= 2:
                    return False
                else:
                    l_count += 1
            else:
                l_count = 0
        return True

