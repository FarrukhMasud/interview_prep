class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        minVal = None
        current = root
        while current:
            minVal = current.val
            current = current.left

        maxVal = None
        current = root
        while current:
            maxVal = current.val
            current = current.right
        diffmin = abs(root.val - minVal)
        diffmax = abs(root.val - maxVal)
        return max(diffmax, diffmin)


# i = TreeNode(
#     8,
#     TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
#     TreeNode(10, None, TreeNode(14, TreeNode(13))),
# )

i = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
result = Solution().maxAncestorDiff(i)
print(result)
