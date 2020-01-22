from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        traversal = dict()
        minLevel, maxLevel = self._verticalOrder(root, 0, traversal, 0, 0, 0)
        result = []
        for i in range(minLevel, maxLevel + 1):
            x = traversal[i]
            x = sorted(x, key=lambda t: t[1])
            y = [q[0] for q in x]
            result.append(y)
        return result

    def _verticalOrder(
        self,
        root: TreeNode,
        level: int,
        traversal,
        minLevel: int,
        maxLevel: int,
        depth: int,
    ):
        if root is None:
            return minLevel, maxLevel
        if level in traversal:
            traversal[level].append((root.val, depth))
        else:
            traversal[level] = [(root.val, depth)]
        temp_min = minLevel
        temp_max = maxLevel
        if root.left is not None:
            temp_min, temp_max = self._verticalOrder(
                root.left, level - 1, traversal, minLevel - 1, maxLevel, depth + 1
            )
        temp_min1 = minLevel
        temp_max1 = maxLevel
        if root.right is not None:
            temp_min1, temp_max1 = self._verticalOrder(
                root.right, level + 1, traversal, minLevel, maxLevel + 1, depth + 1
            )

        return min(temp_min, temp_min1, minLevel), max(maxLevel, temp_max1, temp_max)


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol = Solution()
result = sol.verticalOrder(root)
print(result)
