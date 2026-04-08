class Solution:
    def isPossible(self, piles: List[int], h: int, k: int) -> bool:
        totaltime = 0
        if k==0:
            return False
        for pile in piles:
            print(totaltime)
            if pile%k == 0:
                totaltime += (pile//k)
            else:
                totaltime += ((pile//k) +1)

            if totaltime>h:
                # print('yes')
                return False
        return True if totaltime <= h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ho = h
        l = 0
        h = max(piles)
        ans = -1
        # print(self.isPossible(piles, ho, 12))
        while l<=h:
            m = (l+h)//2
            # print(l, ho, m, ans)
            if self.isPossible(piles, ho, m):
                ans = m
                h = m-1
            else:
                l = m+1
        return ans

