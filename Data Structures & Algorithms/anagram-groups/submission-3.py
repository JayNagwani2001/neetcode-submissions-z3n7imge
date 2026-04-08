class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}

        for s in strs:
            temp = ''.join(sorted(s))
            if temp in hash1:
                hash1[temp].append(s)
            else:
                hash1[temp] = [s]
        

        print(hash1)

        return list(hash1.values())