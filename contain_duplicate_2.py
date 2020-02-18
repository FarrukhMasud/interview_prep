from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        return len(x) != len(nums)


i = [1, 2, 3, 4, 5, 6, 7]
result = Solution().containsDuplicate(i)
print(result)
