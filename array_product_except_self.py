from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        product = 1
        for i in nums:
            if i == 0:
                numZeros = numZeros + 1
            else:
                product = product * i
        if numZeros > 1:
            return [0 for i in nums]
        result = []
        if numZeros == 1:
            for i in nums:
                if i == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            result = [int(product / i) for i in nums]
        return result


arr = [1, 2, 3, 4, 0, 0]
sol = Solution()
result = sol.productExceptSelf(arr)
print(result)
