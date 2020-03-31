class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return float("inf")
        if root.val == target:
            return target

        l = self.closestValue(root.left, target)
        r = self.closestValue(root.right, target)

        ll = abs(target - l)
        rr = abs(target - r)
        vv = abs(target - root.val)
        t = min(ll, vv, rr)
        if t == ll:
            return l
        elif t == rr:
            return r
        else:
            return root.val


i = TreeNode(2147483647)
result = Solution().closestValue(i, 0.0)
print(result)
