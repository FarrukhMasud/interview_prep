class Solution:
    def reverse(self, s):
        output = [None] * len(s)
        index = len(s) - 1
        for c in s:
            output[index] = c
            index -= 1
        return "".join(output)

    def find_missing(self, arr1, arr2):
        if len(arr1) == len(arr2):
            return None
        ar1 = sorted(arr1) if len(arr1) > len(arr2) else sorted(arr2)
        ar2 = sorted(arr1) if len(arr1) < len(arr2) else sorted(arr2)
        index1 = 0
        index2 = 0
        while index1 < len(ar1) and index2 < len(ar2):
            if ar1[index1] != ar2[index2]:
                return ar1[index1]
            index1 += 1
            index2 += 1
        return ar1[index1]


s = "hello world"
result = Solution().reverse(s)
print(result)


arr1 = [1, 2, 4, 7, 8, 9]
arr2 = [1, 2, 4, 6, 7, 8, 9]
result = Solution().find_missing(arr1, arr2)
print(result)
