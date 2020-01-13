def isBadVersion(n: int) -> bool:
    if n >= 2:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        if not isBadVersion(n):
            return -1

        l = 1
        r = n
        while r >= l:
            mid = int(((r - l) / 2) + l)
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1

        return -1


sol = Solution()
result = sol.firstBadVersion(2)
print(result)
