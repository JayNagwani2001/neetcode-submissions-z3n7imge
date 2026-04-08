from copy import deepcopy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force is O(N2) with SC: O(N)

        #optimal #O(N) with SC: O(N)
        n = len(s)
        m = len(t)
        mp = {}
        mi = 10000000
        ans, ans_len = "", 0

        for i in range(m):
            mp[t[i]] = mp.get(t[i], 0) + 1

        count = len(mp)
        print(mp, count)
        i, j = 0, 0

        print(i, j, n, m)
        while i<=j and j<n:
            print(mp, count)

            if s[j] in mp:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count -= 1

            while count == 0:
                if mi > (j-i+1):
                    mi = j-i+1
                    ans = s[i:j+1]
                
                if s[i] in mp:
                    mp[s[i]] += 1
                    if mp[s[i]] > 0:
                        count += 1
                i += 1
            j += 1

        return ans




