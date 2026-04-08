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
        for ele in s:
            if ele-1 not in s:
                curr = 1
                curr_ele = ele+1
                while curr_ele in s:
                    curr += 1
                    # print(ele, curr)
                    curr_ele += 1
                ans = max(ans, curr)

        return ans