class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        ans = 0
        while i<j:
            curr_amount = min(heights[i], heights[j])*(j-i)
            ans = max(ans, curr_amount)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return ans