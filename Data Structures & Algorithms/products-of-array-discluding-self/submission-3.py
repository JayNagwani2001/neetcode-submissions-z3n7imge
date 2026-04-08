class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                continue

            prod *= num 

        if len(nums) == zeroes:
            return [0]*zeroes

        ans = []
        for num in nums:
            if zeroes:
                if num == 0:
                    if zeroes>1:
                        ans.append(0)
                    else:
                        ans.append(prod)
                else:
                    ans.append(0)
            else:
                ans.append(prod//num)

        return ans
