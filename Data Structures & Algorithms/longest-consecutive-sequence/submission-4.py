class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        curr = 0
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     if nums[i] == nums[i-1]+1:
        #         curr += 1
        #     else:
        #         ans = max(ans, curr)
        #         curr = 0
        # ans = max(ans, curr)

        s = set(nums)
        for i in range(len(nums)):
            if nums[i] in s:
                curr = 0
                ele = nums[i]
                while ele in s:
                    curr += 1
                    # s.remove(ele)
                    print(ele, curr)
                    ele += 1
                ans = max(ans, curr-1)

        return ans+1