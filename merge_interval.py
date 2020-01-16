from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None or len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda i: i[0])
        result = []
        x = intervals[0]
        for i in range(1, len(intervals)):
            y = intervals[i]
            if y[0] <= x[1]:
                # merge
                x[1] = max(y[1], x[1])
            else:
                result.append(x)
                x = y
        result.append(x)
        return result


# arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
arr = [[1, 4], [0, 4]]
sol = Solution()
result = sol.merge(arr)
print(result)
