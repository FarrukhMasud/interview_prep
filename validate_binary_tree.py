class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, 214748364700, -214748364700)

    def _isValidBST(self, root: TreeNode, low: int, high: int) -> bool:
        if root is None:
            return True
        if root.val >= low or root.val <= high:
            return False
        return self._isValidBST(
            root.left, min(low, root.val), high
        ) and self._isValidBST(root.right, low, max(high, root.val))


r = TreeNode(2147483647)
# r.left = TreeNode(1)
# r.right = TreeNode(3)
sol = Solution()
result = sol.isValidBST(r)
print(result)
