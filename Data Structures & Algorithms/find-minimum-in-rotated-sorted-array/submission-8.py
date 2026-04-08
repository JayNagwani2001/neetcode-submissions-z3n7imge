class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        n = len(nums)

        if nums[l] <= nums[h]:
            return nums[l]
        #binary search
        while l<=h:
            m = (l+h)//2
            print(l, h, m)

            prev = (m-1+n)%n
            next = (m+1)%n
            if nums[prev] >= nums[m] and nums[m] <= nums[next]:
                return nums[m]
            elif nums[m] <= nums[h]:
                h = m-1
            elif nums[l] <= nums[m]: #always move to unsorted side
                l = m+1
            


        #lower bound solution: min ele is the first ele of rotated portion
        # while l < h:
        #     m = (l + h)//2

        #     if nums[0] <= nums[m]:
        #         l = m+1
        #     else:
        #         h = m

            
        # return nums[h]