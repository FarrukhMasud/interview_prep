class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        if not root:
            return []
        q = [root]
        result = []
        while len(q) > 0:
            n = q.pop(0)
            if n is None:
                result.append(None)
            else:
                result.append(n.val)
                q.append(n.left)
                q.append(n.right)
        while result[-1] is None:
            result.pop()
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or len(data) == 0:
            return None
        root = TreeNode(data.pop(0))
        q = [root]
        while len(data) > 0:
            n = q.pop(0)
            x = data.pop(0)
            y = None
            if len(data) > 0:
                y = data.pop(0)

            if x:
                n.left = TreeNode(x)
                q.append(n.left)
            if y:
                n.right = TreeNode(y)
                q.append(n.right)
        return root


root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
c = Codec()
result = c.serialize(root)
result1 = c.deserialize(result)

print(result)
