class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        lst1 = []
        self._dfsIterate(root1, lst1)
        lst2 = []
        self._dfsIterate(root2, lst2)

        return lst1 == lst2

    def _dfsIterate(self, node: TreeNode, leaves):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        if node.left:
            self._dfsIterate(node.left, leaves)
        if node.right:
            self._dfsIterate(node.right, leaves)


a = TreeNode(1, TreeNode(2), TreeNode(3))
b = TreeNode(1, TreeNode(3), TreeNode(2))
result = Solution().leafSimilar(a, b)
print(result)
