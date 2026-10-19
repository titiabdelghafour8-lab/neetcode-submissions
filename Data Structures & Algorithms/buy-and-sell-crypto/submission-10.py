class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0
        sell = 0
        i = 1
        max_profit = 0
        while i < n and buy <= sell:
            if prices[i] > prices[sell]:
                sell = i
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            max_profit = max(max_profit, prices[sell] - prices[buy])
            i += 1 
        return max_profit



            


    

