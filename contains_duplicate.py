from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums is None or len(nums) == 1:
            return False
        x = dict()
        for i, val in enumerate(nums):
            if val not in x:
                x[val] = []
            x[val].append(i)

        for key in x.keys():
            lst = x[key]
            if len(lst) == 1:
                continue
            a = None
            for i in lst:
                if a is None:
                    a = i
                else:
                    b = i
                    if (b - a) <= k:
                        return True
                    a = b
        return False


sol = Solution()
arr = [1, 0, 1, 1]
result = sol.containsNearbyDuplicate(arr, 1)
print(result)
