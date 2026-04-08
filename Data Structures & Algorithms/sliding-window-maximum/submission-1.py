import heapq 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #using deque:O(N) + O(k)
        dq = deque()
        ans = []
        for i in range(len(nums)):
            #check window size
            if dq and dq[0] <= i-k:
                dq.popleft()
            

            #check if current element is more or not, 
            # then smaller elements will never be used again
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i-k+1 >= 0:
                ans.append(nums[dq[0]])

        return ans


        # ans = []
        # maxis = []
        # i, j = 0, 0

        # while j < len(nums):
        #     #cal
        #     print(i, j)
        #     print(ans)
        #     while maxis and maxis[-1] < nums[j]:
        #         maxis.pop(-1)
            
        #     maxis.append(nums[j])

        #     if j-i+1 < k:
        #         j += 1
            
        #     #slide
        #     if j-i+1 == k:
        #         ans.append(maxis[0])
        #         if maxis[0] == nums[i]:
        #             maxis.pop(0)
        #         i += 1
        #         j += 1
            
        # return ans