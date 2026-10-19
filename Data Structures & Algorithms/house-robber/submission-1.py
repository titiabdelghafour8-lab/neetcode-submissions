class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(i, memo):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return nums[i]
            if i in memo:
                return memo[i]

            for j in range(2, i + 1):
                res = dp(i - j, memo) + nums[i]
                memo[i] = max(memo[i] if i in memo else -1, res)
            return memo[i]

        return max(dp(n - 1, {}), dp(n - 2, {}))
            
            