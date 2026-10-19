class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        n = len(nums)
        
        
        product_not_nul = 1
        for num in nums: 
            if num != 0:
                product_not_nul *= num
        
        result = [0 for _ in range(n)]
        
        if (zero_count == 1):
            result[nums.index(0)] = product_not_nul

        elif (zero_count == 0):
            for i in range(n):
                result[i] = product_not_nul // nums[i]

        return result 
            
            