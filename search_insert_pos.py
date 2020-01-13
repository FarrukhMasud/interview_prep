from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while r >= l:
            mid = int((r + l) / 2)
            m_val = nums[mid]
            if m_val == target:
                return mid
            if m_val > target:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1


sol = Solution()
arr = [3, 4, 5, 6, 7, 8]

result = sol.searchInsert(arr, 6)
print(result)

