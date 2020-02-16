from typing import List
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph or len(paragraph) == 0:
            return ""
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        banned = set([w.lower() for w in banned])
        words = paragraph.lower().split(sep=" ")
        import collections

        w1 = [w for w in words if w not in banned and len(w.strip()) > 0]
        frequency = collections.Counter(w1)

        c = 0
        v = ""
        for k in frequency:
            if len(k.strip()) == 0:
                continue
            if frequency[k] > c:
                c = frequency[k]
                v = k

        return v


para = "Bob. hIt, baLl"

banned = ["hit", "Bob"]
result = Solution().mostCommonWord(para, banned)
print(result)
