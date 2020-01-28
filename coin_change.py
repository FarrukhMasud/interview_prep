from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1
        coins = sorted(coins)
        if amount < coins[0]:
            return -1
        result = [1000000 for i in range(amount + 1)]
        result[0] = 0
        for i in range(1, len(result)):
            for c in coins:
                if i - c >= 0:
                    result[i] = min(result[i - c] + 1, result[i])
        return result[amount] if result[amount] < 1000000 else -1


coins = [186, 419, 83, 408]
amount = 6249
result = Solution().coinChange(coins, amount)
print(result)

