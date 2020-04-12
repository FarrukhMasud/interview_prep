from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return

        index = len(nums) - 2
        while index >= 0:
            if nums[index] < nums[index + 1]:
                break
            index -= 1
        if index < 0:
            nums.sort()
            return
        index_replace = index + 1
        while index_replace < len(nums) - 1:
            if (
                nums[index_replace] > nums[index]
                and nums[index_replace + 1] <= nums[index]
            ):
                break
            index_replace += 1
        temp = nums[index]
        nums[index] = nums[index_replace]
        nums[index_replace] = temp

        nums_to_switch = int((len(nums) - index - 1) / 2)
        for i in range(nums_to_switch):
            temp = nums[index + 1 + i]
            nums[index + 1 + i] = nums[-1 * (i + 1)]
            nums[-1 * (i + 1)] = temp


arr = [1, 5, 1]
Solution().nextPermutation(arr)
print(arr)
