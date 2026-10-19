class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        memo = {}
        def dprec(curr):
            if curr < 0:
                return 0
            if curr in memo:
                return memo[curr]
            if curr == 0:
                return 1

            memo[curr] = dprec(curr - 1) + dprec(curr - 2)
            return memo[curr]

        res = dprec(n)
        return res

        