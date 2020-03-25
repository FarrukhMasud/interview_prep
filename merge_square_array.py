from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
        temp1 = []
        temp2 = []
        result = []
        for i in A:
            if i < 0:
                temp1.append(i * i)
            else:
                temp2.append(i * i)
        temp1 = temp1[::-1]
        while temp1 and temp2:
            if temp1[0] < temp2[0]:
                result.append(temp1.pop(0))
            else:
                result.append(temp2.pop(0))
        if temp1:
            result.extend(temp1)
        if temp2:
            result.extend(temp2)
        return result


i = [-4, -1, 0, 3, 10]
result = Solution().sortedSquares(i)
print(result)
