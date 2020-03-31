class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return self._maxDepth(root, 1)

    def _maxDepth(self, root, level: int) -> int:
        if not root:
            return level
        if not root.children:
            return level
        max_depth = 0
        for c in root.children:
            max_depth = max(max_depth, self._maxDepth(c, level + 1))
        return max_depth
