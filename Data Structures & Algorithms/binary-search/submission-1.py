class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        j = n - 1
        i = 0
        while i <= j:
            middle = (i + j) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                i = middle + 1
            else:
                j = middle - 1    
        return -1