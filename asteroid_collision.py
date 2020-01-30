from typing import List


class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        if not arr or len(arr) == 0:
            return []
        result = []
        while arr and len(arr) > 0 and arr[0] < 0:
            result.append(arr.pop(0))
        if len(arr) == 0:
            return result
        # result1 = []
        # while arr and len(arr) > 0 and arr[-1] > 0:
        #     result1.append(arr.pop(-1))

        # result.extend(result1)
        temp = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] > 0:
                temp.append(arr[i])
            else:
                flag = True
                while len(temp) > 0 and temp[-1] > 0:
                    if (temp[-1]) == abs(arr[i]):
                        temp.pop(-1)
                        flag = False
                        break
                    elif temp[-1] < abs(arr[i]):
                        temp.pop(-1)
                    else:
                        flag = False
                        break
                if flag:
                    temp.append(arr[i])
        result.extend(temp)
        return result


arr = [-2, 1, -2, -2]
result = Solution().asteroidCollision(arr)
print(result)
