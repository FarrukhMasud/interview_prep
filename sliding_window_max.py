from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]
        if k == 1:
            return nums

        result = []
        currentMax = []

        for i in range(0, k):
            while currentMax and currentMax[-1][1] < nums[i]:
                currentMax.pop()
            currentMax.append((i, nums[i]))

        for i in range(k, len(nums)):
            x = currentMax[0]
            result.append(x[1])
            if x[0] <= i - k:
                currentMax.pop(0)
            while currentMax and currentMax[-1][1] < nums[i]:
                currentMax.pop()
            currentMax.append((i, nums[i]))

        x = [i[1] for i in currentMax]
        result.append(max(x))
        return result


nums = [7, 2, 4]
k = 2
result = Solution().maxSlidingWindow(nums, k)
print(result)
