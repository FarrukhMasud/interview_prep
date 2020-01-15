class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        super().__init__()
        self.sum = 0

    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sum = root.val
        self._maxPathSum(root)
        return self.sum

    def _maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l = 0
        if root.left is not None:
            l = self._maxPathSum(root.left)
        r = 0
        if root.right is not None:
            r = self._maxPathSum(root.right)

        self.sum = max(self.sum, root.val + r + l, root.val + r, root.val + l, root.val)
        return max(root.val + r, root.val + l, root.val)


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)
sol = Solution()
result = sol.maxPathSum(root)
print(result)
