class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_loc = dict()
        index1 = 0
        for i, c in enumerate(s):
            if c in char_loc:
                if len(char_loc) > max_length:
                    max_length = len(char_loc)
                index = char_loc[c]
                for j in range(index1, index + 1):
                    if s[j] in char_loc and char_loc[s[j]] == j:
                        char_loc.pop(s[j], None)
                # chars_remove = []
                # for cc in char_loc:
                #     ci = char_loc[cc]
                #     if ci <= index:
                #         chars_remove.append(cc)
                # for ccc in chars_remove:
                #     char_loc.pop(ccc, None)
            char_loc[c] = i
        if len(char_loc) > max_length:
            max_length = len(char_loc)
        return max_length


sol = Solution()
x = sol.lengthOfLongestSubstring("bpfbhmipx")
print(x)
