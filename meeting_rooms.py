from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) <= 0:
            return 0
        if len(intervals) <= 1:
            return 1

        intervals1 = []
        for i in intervals:
            intervals1.append(i[0])
            intervals1.append(-1 * (i[1] - 0.01))

        intervals1 = sorted(intervals1, key=lambda i: abs(i))

        stack = []
        rooms = 0
        maxRooms = -1
        for i in intervals1:
            if i >= 0:
                rooms = rooms + 1
                maxRooms = max(rooms, maxRooms)
            else:
                rooms = rooms - 1
        return maxRooms


sol = Solution()
arr = [[13, 15], [1, 13]]
result = sol.minMeetingRooms(arr)
print(result)
