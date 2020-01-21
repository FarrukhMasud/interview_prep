from typing import List


class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        if arr is None or len(arr) == 1:
            return True
        i = 0
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i = i + 1

        if i >= len(arr) - 2:
            return True

        isIncreasing = arr[i] >= arr[i + 1]
        while i < len(arr) - 1:
            if arr[i] != arr[i + 1]:
                newIncreasing = arr[i] >= arr[i + 1]
                if isIncreasing != newIncreasing:
                    return False
            i = i + 1

        return True


sol = Solution()
arr = [1, 1, 2, 4]
result = sol.isMonotonic(arr)
print(result)
