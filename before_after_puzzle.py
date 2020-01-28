from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        firstWord = dict()

        for phrase in phrases:
            sp = phrase.split(sep=" ")
            if len(sp) == 0:
                continue
            if sp[0] in firstWord:
                firstWord[sp[0]].append(phrase)
            else:
                firstWord[sp[0]] = [phrase]

        result = set()
        for phrase in phrases:
            sp = phrase.split(sep=" ")
            if sp[-1] in firstWord:
                x = " ".join(sp[0:-1])
                y = firstWord[sp[-1]]
                for z in y:
                    result.add((x + " " + z).strip())
        res = [s for s in result]
        return res


arr = [
    "mission statement",
    "a quick bite to eat",
    "a chip off the old block",
    "chocolate bar",
    "mission impossible",
    "a man on a mission",
    "block party",
    "eat my words",
    "bar of soap",
]

# arr = ["a", "b", "a"]
result = Solution().beforeAndAfterPuzzles(arr)
print(result)
