from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nextGen = dict()
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                aliveNieghbours = 0
                for k in directions:
                    new_i = i + k[0]
                    new_j = j + k[1]
                    if (
                        new_i >= 0
                        and new_j >= 0
                        and new_i < len(board)
                        and new_j < len(board[i])
                    ):
                        aliveNieghbours = aliveNieghbours + board[new_i][new_j]
                isAlive = False
                if board[i][j] == 1:
                    if aliveNieghbours == 2 or aliveNieghbours == 3:
                        isAlive = True
                else:
                    if aliveNieghbours == 3:
                        isAlive = True
                nextGen[(i, j)] = isAlive

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                board[i][j] = 1 if nextGen[(i, j)] == True else 0


arr = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

sol = Solution()
sol.gameOfLife(arr)
print(arr)
