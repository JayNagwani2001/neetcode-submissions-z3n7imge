class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for ele in nums:
            if ele in freq:
                return True
            else:
                freq.add(ele)
        return False

         