from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        currentSum = nums[0]
        for j in range(1, len(nums)):
            i = nums[j]
            if currentSum + i < i:
                currentSum = i
            else:
                currentSum += i

            if maxSum < currentSum:
                maxSum = currentSum
        if maxSum < currentSum:
            maxSum = currentSum
        return maxSum


i = [-1, 0, -2]
result = Solution().maxSubArray(i)
print(result)
