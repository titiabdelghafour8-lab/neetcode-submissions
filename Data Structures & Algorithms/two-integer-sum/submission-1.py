class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for k in range(len(nums)):
            value = target - nums[k]
            if nums[k] in values:
                return [values[nums[k]], k]
            values[value] = k
