class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        result = ""
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index = 1
        for w in words:
            tw = ""
            if w[0] in vowels:
                tw = w + "ma"
            else:
                tw = w[1:] + w[0] + "ma"
            result = result + " " + tw + ("a" * index)
            index = index + 1
        return result.strip()


i = "I speak Goat Latin"
result = Solution().toGoatLatin(i)
print(result)
