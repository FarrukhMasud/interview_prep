class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_loc = dict()
        index1 = 0
        for i, c in enumerate(s):
            if c in char_loc:
                length = len(char_loc)
                if length > max_length:
                    max_length = length
                index = char_loc[c]
                for j in range(index1, index + 1):
                    if s[j] in char_loc and char_loc[s[j]] == j:
                        char_loc.pop(s[j], None)
                index1 = index

            char_loc[c] = i
        length = len(char_loc)
        if length > max_length:
            max_length = length
        return max_length


sol = Solution()
# "abcabcbb"
# "`bpfbhmipx`"
x = sol.lengthOfLongestSubstring("abba")
print(x)
