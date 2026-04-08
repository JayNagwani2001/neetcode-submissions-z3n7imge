class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        curr = 0
        nums = sorted(nums)
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
            print(curr)
        ans = max(ans, curr)
        return ans+1