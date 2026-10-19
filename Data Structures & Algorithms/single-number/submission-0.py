class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd = 0
        for i in range(len(nums)):
            odd ^= nums[i]
        return odd
        