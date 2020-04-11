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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        histogram = [0] * len(matrix[0])
        maximal = -1
        for row in matrix:
            curr_histo = []
            for i, v in enumerate(row):
                if v == "0":
                    curr_histo.append(0)
                else:
                    curr_histo.append(1 + histogram[i])
            histogram = curr_histo
            max_rect = self.largestRectangleArea(histogram)
            if maximal < max_rect:
                maximal = max_rect
        return maximal


i = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

result = Solution().maximalRectangle(i)
print(result)
