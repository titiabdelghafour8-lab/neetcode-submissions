class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0 
        while i < n - 1 and nums[i] < nums[i + 1]: 
            i += 1
        return nums[(i + 1) % n]
