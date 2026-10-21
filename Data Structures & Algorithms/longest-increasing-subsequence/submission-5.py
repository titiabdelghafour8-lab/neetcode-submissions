class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        for i in range(n):
            for k in range(i):
                if nums[k] < nums[i]:
                    dp[i + 1] = max(dp[i + 1], dp[k + 1] + 1)
        return max(dp)