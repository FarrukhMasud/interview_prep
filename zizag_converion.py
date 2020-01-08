class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        resultList = ["" for i in range(0, numRows)]

        direction = True
        row = -1
        # col = 0
        for i, c in enumerate(s):
            if direction:
                row = row + 1
                if row >= numRows:
                    direction = False
                    row = row - 2
            else:
                row = row - 1
                if row < 0:
                    row = 1
                    direction = True
            resultList[row] = resultList[row] + c
        result = ""
        for ss in resultList:
            result = result + ss
        return result


#
sol = Solution()
x = sol.convert("PAYPALISHIRING", 2)
print(x)

