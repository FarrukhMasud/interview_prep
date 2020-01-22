from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        queue = deque()
        queue.append((root, 0))
        minLevel = 0
        maxLevel = 0
        levelTraversal = dict()
        result = []
        while len(queue) > 0:
            r = queue.popleft()
            if r[1] in levelTraversal:
                levelTraversal[r[1]].append(r[0].val)
            else:
                levelTraversal[r[1]] = [r[0].val]
            minLevel = min(minLevel, r[1])
            maxLevel = max(maxLevel, r[1])
            if r[0].left:
                queue.append((r[0].left, r[1] - 1))
            if r[0].right:
                queue.append((r[0].right, r[1] + 1))
        for i in range(minLevel, maxLevel + 1):
            result.append(levelTraversal[i])
        return result


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol = Solution()
result = sol.verticalOrder(root)
print(result)
