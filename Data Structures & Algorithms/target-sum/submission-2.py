from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ? what should I do ? add substract ? 
        # what parametres hold the current state ? 
        memo = defaultdict(int)
        def dp(i, current_sum): # i current index in the nums array, current_sum is the reached sum yet
            # dp is the number of ways to reach current_sum starting at index i 
            if i >= len(nums):
                return 0
            if (i == len(nums) - 1) and (current_sum == nums[i] and current_sum == -nums[i]):
                return 2
            if (i == len(nums) - 1) and (current_sum == nums[i] or current_sum == -nums[i]):
                return 1
            
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            
            memo[(i, current_sum)] = dp(i + 1, current_sum - nums[i]) + dp(i + 1, current_sum + nums[i])
            return memo[(i, current_sum)]
        
        return dp(0, target)