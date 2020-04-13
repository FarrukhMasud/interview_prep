from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        level = 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                temp = height[left]
                left += 1
            else:
                temp = height[right]
                right -= 1
            level = max(level, temp)
            result += level - temp
        return result


i = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
r = Solution().trap(i)
print(r)
