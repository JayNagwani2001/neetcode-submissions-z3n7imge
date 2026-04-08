class Solution:
    def trap(self, height: List[int]) -> int:
        #brute force -> SC: O(1) and TC: O(N2)
        leftmax = -1
        rightmax = -1
        ans = 0
        for i in range(1, len(height)):
            for j in range(0, i):
                leftmax = max(leftmax, height[j])
            
            for j in range(i+1, len(height)):
                rightmax = max(rightmax, height[j])

            print(leftmax, rightmax, height[i], ans, i)
            if height[i] < leftmax and height[i] < rightmax:
                ans += min(leftmax, rightmax) - height[i]
            leftmax = -1
            rightmax = -1
        return ans