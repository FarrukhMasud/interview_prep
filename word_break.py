from typing import List
from itertools import filterfalse


class TrieNode:
    def __init__(self, x):
        self.value = x
        self.isTerminal = False
        self.children = dict()

    def add(self, x):
        if x is None:
            return

        c = x[0]
        if c not in self.children:
            y = TrieNode(c)
            self.children[c] = y

        y = self.children[c]
        if len(x) == 1:
            y.isTerminal = True
        else:
            y.add(x[1:])

    def containsNext(self, c) -> bool:
        return c in self.children

    def moveForward(self, c):
        return self.children[c]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = TrieNode("@")
        for w in wordDict:
            words.add(w)

        lst: List[TrieNode] = set()
        lst.add(words)
        for c in s:
            if len(lst) == 0:
                return False
            lst = {t.moveForward(c) for t in lst if t.containsNext(c)}
            xx = {words for w in lst if w.isTerminal}
            if len(xx) > 0:
                lst = lst.union(xx)

        if words in lst:
            return True
        return False


wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "catsandog"
sol = Solution()
result = sol.wordBreak(s, wordDict)
print(result)
