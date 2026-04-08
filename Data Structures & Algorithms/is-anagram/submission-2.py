class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in range(len(s)):
            hash1[s[i]] = hash1.get(s[i], 0) + 1
        
        for i in range(len(t)):
            hash2[t[i]] = hash2.get(t[i], 0) + 1

        for letter in hash1.keys():
            if hash1.get(letter, 0) != hash2.get(letter, 0):
                return False
        for letter in hash2.keys():
            if hash1.get(letter, 0) != hash2.get(letter, 0):
                return False

        return True