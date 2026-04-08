class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # h = [(i, strs[i]) for i in range(len(strs))]
        # # print(h)
        # for i, s in h:
        #     ss = "".join(sorted(s))
        #     h[i] = (i, ss)
        
        # h = sorted(h, key = lambda x:x[1])
        # # print(h)
        # # print(h)
        # prev = h[0][1]
        # ans = [[strs[h[0][0]]]]
        # for ind in range(1, len(h)):
        #     if h[ind][1] == prev:
        #         ans[-1].append(strs[h[ind][0]])
        #     else:
        #         prev = h[ind][1]
        #         ans.append([strs[h[ind][0]]])
        #     print(ans)
        # # print(ans)
        # return ans

        anagram_map = {}

        for word in strs:
            # Sort the word and use it as a key
            key = ''.join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)

        # Return the values of the dictionary as a list of lists
        return list(anagram_map.values())

        