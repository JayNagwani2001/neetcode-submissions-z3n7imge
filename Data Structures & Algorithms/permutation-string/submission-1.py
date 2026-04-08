class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = s2, s1 #s1 is bigger

        n = len(s1)
        m = len(s2)
        if m>n:
            return False
            
        hash1, hash2 = {}, {}

        for i in range(m):
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1

        for i in range(m):
            hash1[s1[i]] = hash1.get(s1[i], 0) + 1

        if hash1 == hash2:
            return True
        print(hash1, hash2)

        for i in range(m, n):
            print(hash1, hash2)
            if hash1 == hash2:
                return True
            else:
                hash1[s1[i-m]] = hash1[s1[i-m]] - 1
                hash1[s1[i]] = hash1.get(s1[i], 0) + 1
                if hash1[s1[i-m]] == 0:
                    del hash1[s1[i-m]]
                    
        if hash1 == hash2:
            return True

        return False
