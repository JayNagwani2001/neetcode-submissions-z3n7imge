class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        
        if nums[l] <= nums[h]:
            return nums[l]

        while l < h:
            m = (l + h)//2

            if nums[0] <= nums[m]:
                l = m+1
            else:
                h = m

            
        return nums[h]