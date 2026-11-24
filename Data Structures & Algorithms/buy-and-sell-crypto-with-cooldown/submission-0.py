from collections import defaultdict
class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        # I like the name NeetCoin
        # I am at day i what can I do ? 
        # either buy a Neetcoin ? or sell the NeetCoin or do nothing
        # when I sell the NeetCoin ? I cannot buy one the next day so I am obliged to go to day i + 2
        # have = True we have a coin have = False we don't 
        memo = defaultdict(int)
        def dp(i, profit, have):
            if i >= len(prices):
                return profit
            if (i, profit, have) in memo:
                return memo[(i, profit)]
            if have:
                memo[(i, profit, have)] = max(
                    dp(i + 1, profit, True), 
                    dp(i + 2, profit + prices[i], False), 
                ) 
            else:
                memo[(i, profit, have)] = max(
                    dp(i + 1, profit, False),
                    dp(i + 1, profit - prices[i], True)
                )
            return memo[(i, profit, have)]
        return dp(0, 0, False) 