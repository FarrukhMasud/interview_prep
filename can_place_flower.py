from typing import List


class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        if not arr or len(arr) == 0:
            return False
        if n <= 0:
            return True
        if len(arr) == 1:
            if arr[0] == 0:
                return True
            else:
                return False
        if arr[0] == 0 and arr[1] == 0:
            n = n - 1
            if n == 0:
                return True
            arr[0] = 1

        for i in range(1, len(arr) - 1):
            if arr[i] == 1:
                continue
            prev = arr[i - 1]
            next = arr[i + 1]
            if prev == 0 and next == 0:
                n = n - 1
                if n == 0:
                    return True
                arr[i] = 1

        if arr[-1] == 0 and arr[-2] == 0:
            if n <= 1:
                return True

        return False


flowerbed = [1, 0, 0, 0, 1]
n = 2
result = Solution().canPlaceFlowers(flowerbed, n)
print(result)
