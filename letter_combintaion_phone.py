from typing import List


class Solution:
    def __init__(self):
        super().__init__()
        self.leters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        return self._lc(digits, 0)

    def _lc(self, digits, index) -> List[str]:
        if (
            index < 0
            or not digits
            or len(digits) == 0
            or index >= len(digits)
            or digits[index] not in self.leters
        ):
            return None

        result = []
        temp = self.leters[digits[index]]
        temp1 = self._lc(digits, index + 1)
        for t in temp:
            if temp1:
                for t1 in temp1:
                    result.append(t + t1)
            else:
                result.append(t)
        return result


n = "232"
result = Solution().letterCombinations(n)
print(result)
