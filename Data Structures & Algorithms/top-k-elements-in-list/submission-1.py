class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)

        h = {}

        for i in range(l):
            h[nums[i]] = h.get(nums[i], 0) + 1
        # print(h)
        h = sorted(h.items(), key=lambda x: x[1], reverse=True)
        # print(h)
        h = [h[i][0] for i in range(k)]

        return h