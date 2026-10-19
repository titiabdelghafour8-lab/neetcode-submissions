class Solution:
    def find_subsets(self, i, nums, subset, res):
        if i == len(nums):
            res.append(list(subset))
            return
        
        subset.append(nums[i])
        self.find_subsets(i + 1, nums, subset, res)

        subset.pop()
        self.find_subsets(i + 1, nums, subset, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.find_subsets(0, nums, subset, res)
        return res 
    