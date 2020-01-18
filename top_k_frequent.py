from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        x = dict()
        for i in nums:
            if i in x:
                x[i] = x[i] + 1
            else:
                x[i] = 1
        y = []
        for i in x.keys():
            y.append((i, x[i]))
        z = sorted(y, key=lambda w: w[1])
        a = [v[0] for v in z[len(z) - k : len(z)]]
        return a


sol = Solution()
arr = [-1, -1]

result = sol.topKFrequent(arr, 1)
print(result)
