class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1, f2 = {}, {}

        for ch in s:
            if ch not in f1:
                f1[ch] = 1
            else:
                f1[ch] += 1
        
        for ch in t:
            if ch not in f2:
                f2[ch] = 1
            else:
                f2[ch] += 1

        for ch in f1.keys():
            if ch not in f2:
                return False
                
            if f1[ch] != f2[ch]:
                return False
            

        return len(f1) == len(f2)

        
                 