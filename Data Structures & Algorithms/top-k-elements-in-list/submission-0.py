class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #bucket sort algo: O(n)
        #freq as a index of list

        f = {}
        for num in nums:
            f[num] = f.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for (key, freq) in f.items():
            bucket[freq].append(key)

        ans = []

        for b in bucket[::-1]:
            if len(b):
                ans.extend(b)    


        return ans[:k]

        