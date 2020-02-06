from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] != k:
            return 0
        count = 0
        x = 0
        sumD = defaultdict(list)
        sumD[0].append(1)
        for i, iv in enumerate(nums):
            x += iv

            if x - k in sumD:
                count += len(sumD[x - k])
            sumD[x].append(i)
        return count


nums = [-1, -1, 1]
k = 0
result = Solution().subarraySum(nums, k)
print(result)
