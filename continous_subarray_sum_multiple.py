from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        k = abs(k)
        if not nums or len(nums) < 2:
            return False
        if len(nums) == 1 and nums[0] != k:
            return False
        if sum(nums) == k:
            return True

        s = 0
        sums = []
        prev = None
        for i, v in enumerate(nums):
            s += v
            sums.append(s)

        for i, v in enumerate(sums):
            for j in range(i + 1, len(nums)):
                s = sums[j] - v + nums[i]
                if s == k or (k > 0 and int(s % k) == 0):
                    return True

        return False


nums = [23, 2, 6, 4, 7]
k = 0
result = Solution().checkSubarraySum(nums, k)
print(result)
