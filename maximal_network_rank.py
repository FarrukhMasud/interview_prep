from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = [[0] * n for i in range(n)]
        for r in roads:
            connected[r[0]][r[1]] = 1
            connected[r[1]][r[0]] = 1
        cities = [sum(i) for i in connected]
        maximal = 0
        for i in range(n):
            i_conn = cities[i]
            for j in range(i + 1, n):
                j_conn = cities[j]
                if connected[i][j] != 0:
                    j_conn -= 1
                maximal = max(maximal, i_conn + j_conn)

        return maximal


inputs = [
    (4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4),
    (5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]], 5),
    (8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]], 5),
]

sol = Solution()
for i in inputs:
    res = sol.maximalNetworkRank(i[0], i[1])
    if i[2] != res:
        print(
            "Error --- reciedved : {}\t expected:{} \t input:{}".format(res, i[2], i[1])
        )
    else:
        print("Success -- {}".format(i[1]))
