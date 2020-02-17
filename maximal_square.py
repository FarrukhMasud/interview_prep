from typing import List


class Solution:
    def maximalSquare(self, m1: List[List[str]]) -> int:
        if not m1 or len(m1) == 0:
            return 0
        matrix = []
        for i in m1:
            matrix.append([])
            for j in i:
                matrix[-1].append(0 if j == "0" else 1)
        maxLength = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    if maxLength == 0:
                        maxLength = 1
                    continue
                matrix[i][j] = (
                    min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j]) + 1
                )
                if matrix[i][j] > maxLength:
                    maxLength = matrix[i][j]
        return maxLength * maxLength


# input = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"],
# ]
input = [["0", "1"]]
result = Solution().maximalSquare(input)
print(result)
