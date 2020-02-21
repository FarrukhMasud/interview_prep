from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        q = [root, None]
        result = [root.val]
        flag = True
        while q:
            n = q.pop(0)
            if not n:
                if len(q) > 0:
                    q.append(n)
                    result.append(q[0].val)
            else:
                # result.append(n.val)
                if n:
                    if n and n.right:
                        q.append(n.right)
                    if n and n.left:
                        q.append(n.left)

        return result


# r = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
r = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
result = Solution().rightSideView(r)
print(result)
