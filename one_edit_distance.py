class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        # check for size difference
        ls = len(s)
        lt = len(t)
        if abs(ls - lt) > 1:
            return False
        arrLong = list(s) if ls > lt else list(t)
        arrShort = list(t) if ls > lt else list(s)
        changeMade = False
        for i, c in enumerate(arrShort):
            if len(arrLong) == 0:
                return False
            temp = arrLong[0]
            if c == temp:
                arrLong.pop(0)
                continue
            else:
                if changeMade:
                    return False
                changeMade = True
                arrLong.pop(0)
                # same length then we have to replace
                if ls != lt:
                    t = arrLong.pop(0)
                    if c != t:
                        return False

        if changeMade and len(arrLong) > 0:
            return False
        return True


s = "a"
t = ""
result = Solution().isOneEditDistance(s, t)
print(result)
