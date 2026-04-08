class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = [(i, strs[i]) for i in range(len(strs))]
        # print(h)
        for i, s in h:
            ss = "".join(sorted(s))
            h[i] = (i, ss)
        
        h = sorted(h, key = lambda x:x[1])
        # print(h)
        # print(h)
        prev = h[0][1]
        ans = [[strs[h[0][0]]]]
        for ind in range(1, len(h)):
            if h[ind][1] == prev:
                ans[-1].append(strs[h[ind][0]])
            else:
                prev = h[ind][1]
                ans.append([strs[h[ind][0]]])
            print(ans)
        # print(ans)
        return ans

        