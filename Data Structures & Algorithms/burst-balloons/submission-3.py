import functools
from collections import defaultdict

class Solution:    
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @functools.cache
        def dp(l, r):
            if l > r:
                return 0
            res = 0
            for i in range(l, r + 1):
                res = max(res, nums[l - 1] * nums[i] * nums[r + 1] + dp(l, i - 1) + dp(i + 1, r))
            return res


        return dp(1, n)





