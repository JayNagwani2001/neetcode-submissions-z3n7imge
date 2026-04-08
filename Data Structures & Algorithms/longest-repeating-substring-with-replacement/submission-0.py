class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = [0]*26
        ans = 0
        i = 0
        
        for j in range(0, len(s)):
            h[ord(s[j]) - ord('A')] += 1
            #shrink
            while (j-i+1) - max(h) > k:
                h[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            # h[ord(s[j]) - ord('A')] += 1
            ans = max(ans, j-i+1)
            print(h)
        return ans


