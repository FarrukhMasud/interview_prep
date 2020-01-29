from typing import List


class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        lisLength = [1] * len(arr)
        counts = [1] * len(arr)
        for i, i_v in enumerate(arr):
            for j in range(0, i):
                if i_v > arr[j]:
                    # lisLength[i] = max(lisLength[j] + 1, lisLength[i])
                    if lisLength[i] <= lisLength[j]:
                        lisLength[i] = lisLength[j] + 1
                        counts[i] = counts[j]
                    elif lisLength[j] + 1 == lisLength[i]:
                        counts[i] += counts[j]

        longest = max(lisLength)
        result = 0
        for i, c in enumerate(lisLength):
            if c == longest:
                result+=counts[i]

        return result


arr = [1, 3, 5, 4, 7]
result = Solution().findNumberOfLIS(arr)
print(result)
