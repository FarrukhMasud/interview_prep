class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        hourArm = (hour * 30) + (minutes * 0.5)
        minuteArm = minutes * 6.0
        diff = abs(hourArm - minuteArm)
        return min(diff, 360 - diff)


input = [
    (1, 57, 76.5),
    (12, 30, 165),
    (3, 30, 75),
    (3, 15, 7.5),
    (4, 50, 155),
    (12, 0, 0),
]


def getStr(i):
    return str(i[0]) + ":" + str(i[1]) + "\t" + str(i[2])


s = Solution()
for i in input:
    an = s.angleClock(i[0], i[1])
    if an == i[2]:
        print("Test passed\t" + getStr(i))
    else:
        print("Test failed\t" + getStr(i) + "\t" + str(an))
