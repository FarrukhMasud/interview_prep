from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchMin(nums, target), self.searchMax(nums, target)]

    def searchMax(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l and l >= 0 and r < len(nums):
            mid = int(((r - l) / 2) + l)
            m_val = nums[mid]
            if m_val > target:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0 or r >= len(nums):
            return -1

        if nums[r] == target:
            return r
        return -1

    def searchMin(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            mid = int(((r - l) / 2) + l)
            m_val = nums[mid]
            if m_val >= target:
                r = mid - 1
            else:
                l = mid + 1

        if l < 0 or l >= len(nums):
            return -1
        if nums[l] == target:
            return l
        return -1


arr = [5, 7, 7, 8, 8, 10]
sol = Solution()
result = sol.searchRange(arr, 7)
# result = sol.searchMax(arr, 8)
print(result)

