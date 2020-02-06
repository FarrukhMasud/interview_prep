from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        count = 0
        x = 0
        for i, _ in enumerate(nums):
            iv = nums[i]
            x = 0
            for j in range(i, len(nums)):
                x += nums[j]
                if x == k:
                    count += 1

        return count


nums = [1, 1, 1]
k = 2
result = Solution().subarraySum(nums, k)
print(result)
