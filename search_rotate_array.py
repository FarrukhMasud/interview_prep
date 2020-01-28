from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if arr[left] == target:
                return left
            if arr[right] == target:
                return right
            if arr[mid] == target:
                return mid

            if arr[left] < arr[mid]:
                if arr[mid] > target and arr[left] < target:
                    right = right - 1
                else:
                    left = left + 1
            else:
                if arr[mid] > target:
                    right = right - 1
                else:
                    left = left + 1

        return -1


nums = [1]
target = 1
result = Solution().search(nums, target)
print(result)
