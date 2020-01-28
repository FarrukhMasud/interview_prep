from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            else:
                temp = prices[i] - minPrice
                if temp > maxProfit:
                    maxProfit = temp
        return maxProfit if maxProfit > 0 else 0


arr = [7, 1, 5, 3, 6, 4]
sol = Solution()
result = sol.maxProfit(arr)
print(result)
