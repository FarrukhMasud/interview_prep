class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        visited = set()
        pt = preorder.split(",")
        right = self._isValidSerialization(pt, 0, visited)

        if right < 0 or len(visited) != len(pt):
            return False
        if len(visited.intersection(range(0, len(pt)))) < len(pt):
            return False
        return True

    def _isValidSerialization(self, preorder, index: int, visited) -> int:
        if index in visited or index >= len(preorder):
            return -1
        visited.add(index)
        if preorder[index] == "#":
            return index
        left = self._isValidSerialization(preorder, index + 1, visited)
        if left < 0:
            return -1
        right = self._isValidSerialization(preorder, left + 1, visited)
        if right < 0:
            return -1
        return right


input = "9,#"
result = Solution().isValidSerialization(input)
print(result)
