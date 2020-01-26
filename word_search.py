from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0 or not word:
            return True
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                visited = set()
                res = self.search(board, i, j, word, 0, visited)
                if res:
                    return True

        return False

    def search(self, board, i, j, word, index, visited):
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[i])
            or index >= len(word)
            or (i, j) in visited
            or board[i][j] != word[index]
        ):
            return False
        if index == len(word) - 1:
            return True
        visited.add((i, j))
        result = (
            self.search(board, i - 1, j, word, index + 1, visited)
            or self.search(board, i + 1, j, word, index + 1, visited)
            or self.search(board, i, j - 1, word, index + 1, visited)
            or self.search(board, i, j + 1, word, index + 1, visited)
        )
        visited.remove((i, j))
        return result


s = "ABCESEEE"
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]

sol = Solution()
result = sol.exist(board, s)
print(result)
