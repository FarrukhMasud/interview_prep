class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while right > left and not result[right].isalpha():
                right -= 1
            if left >= right:
                break
            while right > left and not result[left].isalpha():
                left += 1
            if left >= right:
                break
            temp = result[left]
            result[left] = result[right]
            result[right] = temp
            left += 1
            right -= 1
        return "".join(result)


s = "7_28]"
result = Solution().reverseOnlyLetters(s)
print(result)
