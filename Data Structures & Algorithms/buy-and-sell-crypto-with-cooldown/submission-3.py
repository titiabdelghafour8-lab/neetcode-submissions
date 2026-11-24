from functools import cache


class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i: int, have: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, have) in memo:
                return memo[(i, have)]
            if have:
                memo[(i, have)] = max(
                    dp(i + 1, True),
                    prices[i] + dp(i + 2, False),
                )
            else:
                memo[(i, have)] = max(
                    dp(i + 1, False),
                    -prices[i] + dp(i + 1, True),
                )
            return memo[(i, have)]
        return dp(0, False)