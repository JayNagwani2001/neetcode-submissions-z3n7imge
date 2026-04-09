class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        start = 0
        max_len = 0
        for i in range(n-1, -1, -1):
                for j in range(i, n):
                        if s[i] == s[j]:
                                if j-i <= 2:
                                        dp[i][j] = True
                                else:
                                        dp[i][j] = dp[i+1][j-1]

        ans = 0
        for i in range(n-1, -1, -1):
                for j in range(i, n):
                        if dp[i][j]:
                                ans += 1
        return ans