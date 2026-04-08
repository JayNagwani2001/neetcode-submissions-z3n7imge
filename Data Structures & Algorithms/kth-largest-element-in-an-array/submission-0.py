import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        klargest = heapq.nlargest(k, nums)

        return klargest[-1]
