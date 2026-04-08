import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.pq = nums[:k]
        heapq.heapify(self.pq)
        print(self.pq)

    def add(self, val: int) -> int:
        # min_ele = self.pq[0]#top element
        # if val > min_ele:
        #     heapq.heappop(self.pq)
        #     heapq.heappush(self.pq, val)

        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        print(self.pq)
        return self.pq[0]

