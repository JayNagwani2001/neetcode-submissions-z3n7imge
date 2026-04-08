class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        # elif s == " ":
        #     return 
        ml = 1
        h = {}
        i=0
        h[s[0]] = 1
        for j in range(1, len(s)):
            if s[j] in h:
                while s[j] in h:
                    del h[s[i]]
                    i += 1
            h[s[j]] = 1
            ml = max(ml, j-i+1)

        return ml
