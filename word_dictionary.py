class Node:
    def __init__(self, x):
        self.value = x
        self.isTerminal = False
        self.children = dict()

    def add(self, x):
        if x is None:
            return

        c = x[0]
        if c not in self.children:
            y = Node(c)
            self.children[c] = y

        y = self.children[c]
        if len(x) == 1:
            y.isTerminal = True
        else:
            y.add(x[1:])

    def search(self, x):
        if x is None:
            return False
        if len(x) == 0:
            return self.isTerminal
        c = x[0]
        if c == ".":
            z = x[1:]
            for child_key in self.children:
                child = self.children[child_key]
                if child.search(z):
                    return True
            return False
        else:
            if c not in self.children:
                return False
            y = self.children[c]
            return y.search(x[1:])


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node("@")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.node.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.node.search(word)


sol = WordDictionary()
sol.addWord("a")
sol.addWord("ad")
# sol.addWord("mad")
result = sol.search(".a")
print(result)
