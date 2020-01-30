from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
            not wordList
            or len(wordList) == 0
            or not beginWord
            or not endWord
            or len(beginWord) != len(endWord)
        ):
            return 0
        dictionary = set(wordList)
        d1 = dict()
        for i in range(0, len(wordList[0])):
            for w in wordList:
                if i in d1:
                    d1[i].append(w[i])
                else:
                    d1[i] = [w[i]]

        wordsAlreadyVisited = set()
        wordsAlreadyVisited.add(beginWord)
        beginWord = list(beginWord)
        endWord = list(endWord)
        q = [(beginWord, 1)]

        while len(q) > 0:
            d = q.pop(0)
            bw = d[0]
            t = d[1]
            if bw == endWord:
                return t

            for i in range(0, len(bw)):
                for c in d1[i]:
                    temp = bw.copy()
                    temp[i] = c
                    strTemp = "".join(temp)
                    if temp == endWord:
                        return t + 1
                    if strTemp not in wordsAlreadyVisited and strTemp in dictionary:
                        wordsAlreadyVisited.add(strTemp)
                        q.append((temp, t + 1))

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
result = Solution().ladderLength(beginWord, endWord, wordList)
print(result)
