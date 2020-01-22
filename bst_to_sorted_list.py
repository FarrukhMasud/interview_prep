class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        head = self._treeToDoublyList(root)
        first = head
        while first.left is not None:
            first = first.left
        last = head
        while last.right is not None:
            last = last.right
        first.left = last
        last.right = first
        return first

    def _treeToDoublyList(self, root: "Node") -> "Node":
        if root is None:
            return None
        left = self._treeToDoublyList(root.left)
        right = self._treeToDoublyList(root.right)
        root.left = None
        root.right = None

        if left is not None:
            # left.right = root
            while left.right is not None:
                left = left.right
            root.left = left
            left.right = root
        if right is not None:
            while right.left is not None:
                right = right.left
            right.left = root
            root.right = right

        return root


root = Node(4, Node(2, Node(1), Node(3)), Node(5))
sol = Solution()
result = sol.treeToDoublyList(root)
print(result)
