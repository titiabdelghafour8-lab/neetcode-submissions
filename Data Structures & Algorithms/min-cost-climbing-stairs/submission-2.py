from collections import OrderedDict

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def min_cost(floor, memo):
            if floor < 0:
                return 0
            if floor == 0 or floor == 1:
                return cost[floor]
            if floor in memo:
                return memo[floor]
            memo[floor] = min(min_cost(floor - 1, memo), min_cost(floor - 2, memo)) + (0 if floor == n else cost[floor])
            return memo[floor]
        
        res = min_cost(n, {})
        return res

            
            