class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1) # 0 included
        dp[0] = 1
        for c in coins:
            for a in range(1, amount + 1):
                if a < c:
                    continue
                dp[a] += dp[a - c]
        return dp[amount]


                


