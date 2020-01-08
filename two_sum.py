class Solution:
    def twoSum(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            if sum > target:
                right = right - 1
            else:
                left = left + 1


sol = Solution()
y = [8, 9, 1, 2, 3, 4, 5, 6]
y.sort()
x = sol.twoSum(y, 4)
print(x)
