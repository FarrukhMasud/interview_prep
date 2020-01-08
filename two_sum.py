class Solution:
    def twoSum(self, nums, target: int):
        candidates = dict()
        for i in range(0, len(nums)):
            required = target - nums[i]
            if required in candidates:
                result = [candidates[required], i]
                return result
            candidates[nums[i]] = i


sol = Solution()
y = [8, 9, 1, 2, 3, 4, 5, 6]
y.sort()
x = sol.twoSum(y, 4)
print(x)
