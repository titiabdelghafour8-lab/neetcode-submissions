class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, path):
            res.append(path[:])
            for k in range(i, len(nums)):
                if k > i and nums[k] == nums[k - 1]:
                    continue
                path.append(nums[k])
                backtrack(k + 1, path)
                path.pop()
        backtrack(0, [])
        return res
        