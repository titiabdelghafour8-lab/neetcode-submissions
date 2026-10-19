class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]: 
        res = []
        nums.sort()
        def check_sum(i, cur, summing):
            if summing == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if summing + nums[j] > target:
                    return
                cur.append(nums[j])
                check_sum(j, cur, summing + nums[j])
                cur.pop()
        check_sum(0, [], 0)
        return res
        