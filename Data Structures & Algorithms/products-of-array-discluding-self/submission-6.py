class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result_right = [1] * n
        for i in range(1, n):
            result_right[i] = result_right[i - 1] * nums[i - 1]
        
        result_left = [1] * n
        for j in range(n-2, -1, -1):
            result_left[j] = result_left[j + 1] * nums[j + 1]

        return [ result_left[i] * result_right[i] for i in range(n) ]
            



