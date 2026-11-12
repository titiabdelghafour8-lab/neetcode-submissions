class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max_sbr = nums[0]
        res = max_sbr
        for i in range(1, n):
            if nums[i] > (max_sbr + nums[i]):
                max_sbr = nums[i]
            else:
                max_sbr += nums[i]
            res = max(res, max_sbr)
        return res
        