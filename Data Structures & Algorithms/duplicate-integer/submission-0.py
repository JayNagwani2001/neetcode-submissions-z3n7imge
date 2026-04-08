class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for ele in nums:
            if ele in freq:
                return True
            else:
                freq[ele] = 1
        return False

         