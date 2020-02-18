class Solution:
    def findClosest(self, arr, target):
        if not arr or len(arr) == 0:
            return None
        arr = sorted(arr)
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = int((left + right) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                right = mid - 1
            else:
                left = left + 1
        return left


input = [1, 2, 4, 5, 9, 13]
result = Solution().findClosest(input, 8)
print(result)
print(input[result])
