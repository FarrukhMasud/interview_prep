from typing import List


class TreeNode:
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.children = set()


class Solution:
    def __init__(self):
        super().__init__()
        self.nodes = dict()

    def _visit(self, root, result_stack, visited_set):
        if not root or root in visited_set:
            return
        visited_set.add(root)
        for child in root.children:
            if child not in visited_set:
                self._visit(child, result_stack, visited_set)
        result_stack.append(root.val)

    def alienOrder(self, words: List[str]) -> str:
        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] != words[i - 1][j]:
                    break
            if j == len(words[i]) or j == len(words[i - 1]):
                continue
            if words[i - 1][j] not in self.nodes:
                self.nodes[words[i - 1][j]] = TreeNode(words[i - 1][j])
            if words[i][j] not in self.nodes:
                self.nodes[words[i][j]] = TreeNode(words[i][j])
            self.nodes[words[i - 1][j]].children.add(self.nodes[words[i][j]])

        result_stack = []
        visited_set = set()
        for k in self.nodes:
            self._visit(self.nodes[k], result_stack, visited_set)

        return "".join(result_stack[::-1])


i = ["wrt", "wrf", "er", "ett", "rftt"]
# i = ["z", "x", "z"]
result = Solution().alienOrder(i)
print(result)
