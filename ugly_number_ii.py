class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num = [-1] * n
        ugly_num[0] = 1
        i2 = 0
        i3 = 0
        i5 = 0
        index = 1
        for index in range(1, n):
            n2 = ugly_num[i2] * 2
            n3 = ugly_num[i3] * 3
            n5 = ugly_num[i5] * 5

            ni = min(n2, n3, n5)
            if ni == n2:
                i2 += 1
            if ni == n3:
                i3 += 1
            if ni == n5:
                i5 += 1

            ugly_num[index] = ni
            index += 1
        return ugly_num[-1]
