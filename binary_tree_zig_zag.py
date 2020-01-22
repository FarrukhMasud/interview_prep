from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root, None])
        result = []
        temp = []
        left_to_right = False
        while len(queue) > 0:
            r = queue.popleft()
            if r is None:
                result.append(temp)
                temp = []
                left_to_right = not left_to_right
                if len(queue) > 0:
                    queue.append(None)
            else:
                temp.append(r.val)
                self._appendIfNonNone(r.left, queue)
                self._appendIfNonNone(r.right, queue)
        if len(temp) > 0:
            result.append(temp)

        for i in range(1, len(result), 2):
            result[i] = result[i][::-1]
        return result

    def _appendIfNonNone(self, t, q):
        if t is not None:
            q.append(t)


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
sol = Solution()
result = sol.zigzagLevelOrder(root)
print(result)
