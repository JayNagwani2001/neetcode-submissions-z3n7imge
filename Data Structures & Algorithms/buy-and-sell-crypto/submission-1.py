class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##### O(n2) approach #######
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j]-prices[i])

        # return max_profit

        ##### O(n) approach #######

        max_profit = 0
        i = 0
        end_day = 0
        for j in range(1, len(prices)):
            if prices[i]>prices[j]:
                i = j
            else:
                if max_profit<(prices[j]-prices[i]):
                    max_profit = prices[j]-prices[i]
                    end_day = j
        print(i, end_day)

        return max_profit
