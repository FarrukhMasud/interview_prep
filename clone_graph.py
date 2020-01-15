class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None
        cache = dict()

        def _cloneGraph(node: "Node"):
            if node is None or node in cache:
                return
            cache[node] = Node(node.val)
            for i in node.neighbors:
                if i not in cache:
                    _cloneGraph(i)
                cache[node].neighbors.append(cache[i])

        _cloneGraph(node)
        return cache[node]
