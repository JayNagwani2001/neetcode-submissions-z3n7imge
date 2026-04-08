class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i, ele in enumerate(nums):
            if ele in hash1:
                hash1[ele] = (hash1.get(ele)[0] + 1, hash1.get(ele)[1])
                hash1[ele][1].append(i)
            else:
                hash1[ele] = (1, [i])

        res = []
        print(hash1)

        for i, ele in enumerate(nums):
            need = target-ele
            print(ele, need)

            if need in hash1:

                if need == ele: 
                    if hash1[need][0] == 2:
                        return [i, hash1[need][1][-1]]
                else:
                    return [i, hash1[need][1][-1]]

            else:
                continue


