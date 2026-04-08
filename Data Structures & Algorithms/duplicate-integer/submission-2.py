class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1 = set()
        for ele in nums:
            if ele in hash1:
                return True
            else:
                hash1.add(ele)
        
        return False