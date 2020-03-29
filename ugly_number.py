class Solution:
    def isUgly(self, num: int) -> bool:
        x = num
        divisor = [2, 3, 5]
        while x > 1:
            flag = True
            for y in divisor:
                if x % y == 0:
                    x = x / y
                    flag = False
            if flag:
                return False
        return True


print(Solution().isUgly(51799))
