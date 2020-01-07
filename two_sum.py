class Solution:
    def twoSum(self, nums, target: int):
        candidates = dict()
        for i in range(0, len(nums)):
            required = target - nums[i]
            if required in candidates:
                result = [i, candidates[required]]
                result.sort()
                return result
            candidates[nums[i]] = i


sol = Solution()
x = sol.twoSum([8, 9, 1, 2, 3, 4, 5, 6], 4)
print(x)
