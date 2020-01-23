class Solution:
    def numberToWords(self, num: int) -> str:
        exp = 1000 * 1000 * 1000
        word_billion = ["Billion", "Million", "Thousand"]
        index = 0
        result = ""
        while exp >= 1000:
            c = int(num / exp)
            if c > 0:
                res = self._numberToHundredWords(c)
                result = result + " " + res + " " + word_billion[index]
                num = int(num % exp)
            index = index + 1
            exp = exp / 1000
        result = result + " " + self._numberToHundredWords(num)
        return result.strip()

    def _numberToHundredWords(self, num: int) -> str:
        if num >= 1000:
            raise "The number should have been less than 1000"
        words = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
            "Twenty",
        ]

        words_ten = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        result = ""
        c = int(num / 100)
        if c > 0:
            result = words[c] + " Hundred"
            num = int(num % 100)
        if num < 20 and num > 0:
            result = result + " " + words[num]
        else:
            c = int(num / 10)
            result = result + " " + words_ten[c]
            x = int(num % 10)
            result = result + " " + words[x]
        return result.strip()


num = 1001
sol = Solution()
result = sol.numberToWords(num)
print(result)
