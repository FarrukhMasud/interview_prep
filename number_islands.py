from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] != "1":
                    continue
                self._expand(grid, i, j)
                islands += 1
        return islands

    def _expand(self, grid: List[List[str]], r: int, c: int):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] != "1":
            return
        grid[r][c] = "-1"
        self._expand(grid, r - 1, c)
        self._expand(grid, r + 1, c)
        self._expand(grid, r, c - 1)
        self._expand(grid, r, c + 1)


i = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "1", "1", "1"],
]


result = Solution().numIslands(i)
print(result)
