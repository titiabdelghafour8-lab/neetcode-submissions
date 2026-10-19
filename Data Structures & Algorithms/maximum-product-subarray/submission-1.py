class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1
        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
            temp = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(cur_min * n, temp, n)
            res = max(res, cur_max, cur_min)
        return res
            

            
            
            