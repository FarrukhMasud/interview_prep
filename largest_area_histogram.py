from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stck = []
        largest = -1
        for i, h in enumerate(heights):
            if not stck:
                stck.append((i, h))
            elif h > stck[-1][1]:
                stck.append((i, h))
            elif h < stck[-1][1]:
                pi = 0
                while stck and h < stck[-1][1]:
                    prev = stck.pop(-1)
                    pi = prev[0]
                    area = prev[1] * ((i + 1) - (pi + 1))
                    if largest < area:
                        largest = area
                stck.append((pi, h))

        while stck:
            prev = stck.pop(-1)
            area = prev[1] * (len(heights) - (prev[0]))
            if largest < area:
                largest = area
            i = prev[0]
        return largest


i = [2, 0, 5, 6, 2, 3]
result = Solution().largestRectangleArea(i)
print(result)
