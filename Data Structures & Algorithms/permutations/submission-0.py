class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =  []
        traversed = { num: False for num in nums }
        def sub_permute(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            for k in range(len(nums)):
                if not traversed[nums[k]]:
                    cur.append(nums[k])
                    traversed[nums[k]] = True
                    sub_permute(i + 1, cur)
                    cur.pop()
                    traversed[nums[k]]= False
        sub_permute(0, [])
        return res
                
            

        