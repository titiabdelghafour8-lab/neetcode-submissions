class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        odd = n
        for i in range(n):
            odd ^= i ^ nums[i]
        return odd
        