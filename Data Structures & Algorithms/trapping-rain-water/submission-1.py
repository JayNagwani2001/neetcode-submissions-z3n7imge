class Solution:
    def trap(self, height: List[int]) -> int:
        #brute force -> SC: O(1) and TC: O(N2)
        # leftmax = -1
        # rightmax = -1
        # ans = 0
        # for i in range(1, len(height)):
        #     for j in range(0, i):
        #         leftmax = max(leftmax, height[j])
            
        #     for j in range(i+1, len(height)):
        #         rightmax = max(rightmax, height[j])

        #     print(leftmax, rightmax, height[i], ans, i)
        #     if height[i] < leftmax and height[i] < rightmax:
        #         ans += min(leftmax, rightmax) - height[i]
        #     leftmax = -1
        #     rightmax = -1

        #optimal: TC=SC=O(N) by maintaining prefmax and suffixmax
        L = len(height)
        ans= 0
        prefmax = [-1]*L
        suffixmax = [-1]*L
        prefmax[0] = height[0]
        for i in range(1, len(height)):
            prefmax[i] = max(prefmax[i-1], height[i])
        
        suffixmax[L-1] = height[L-1]
        for i in range(len(height)-2, -1, -1):
            suffixmax[i] = max(suffixmax[i+1], height[i])

        print(prefmax, suffixmax)
        for i in range(L):
            leftmax = prefmax[i]
            rightmax = suffixmax[i]

            if height[i] < leftmax and height[i] < rightmax:
                    ans += min(leftmax, rightmax) - height[i]

        return ans