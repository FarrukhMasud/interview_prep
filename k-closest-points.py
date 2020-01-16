from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sorted_list = sorted(points, key=lambda i: (i[0] * i[0]) + (i[1] * i[1]))
        return sorted_list[:K]

