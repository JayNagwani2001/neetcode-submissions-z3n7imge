class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force: O(NlogN) --> hashing + sorting
        l = len(nums)
        h = {}
        for i in range(l):
            h[nums[i]] = h.get(nums[i], 0) + 1
        # # print(h)
        # h = sorted(h.items(), key=lambda x: x[1], reverse=True)
        # # print(h)
        # h = [h[i][0i] for i in range(k)]
        # -------------------------------------------------------------

        #bucket sort: TC: O(N) + SC: O(N)
        freq = [[] for i in range(l+1)]

        for n, c in h.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) >= k:
                    return res

        return res