from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums is None or len(nums) == 0:
            return []
        result = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if temp[-1] + 1 == nums[i]:
                temp.append(nums[i])
            else:
                if len(temp) == 1:
                    result.append(str(temp[0]))
                else:
                    result.append(str(temp[0]) + "->" + str(temp[-1]))
                temp.clear()
                temp.append(nums[i])
        if len(temp) > 0:
            if len(temp) == 1:
                result.append(str(temp[0]))
            else:
                result.append(str(temp[0]) + "->" + str(temp[-1]))
        return result


arr = [2, 3, 4]
sol = Solution()
result = sol.summaryRanges(arr)
print(result)
