from typing import List


class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        lisLength = [1] * len(arr)

        for i, i_v in enumerate(arr):
            for j in range(0, i):
                if i_v > arr[j]:
                    lisLength[i] = max(lisLength[j] + 1, lisLength[i])

        longest = max(lisLength)
        return longest


arr = [10, 9, 2, 5, 3, 7, 101, 18]
result = Solution().lengthOfLIS(arr)
print(result)
