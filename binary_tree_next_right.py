class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        q = [root, None]
        while q:
            item = q.pop(0)
            if item:
                item.next = q[0]
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                if not q:
                    break
                q.append(item)
        return root


i = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

result = Solution().connect(i)
print(result)
