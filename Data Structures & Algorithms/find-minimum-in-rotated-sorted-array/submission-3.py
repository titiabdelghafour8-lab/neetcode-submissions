class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        j = n - 1 
        min_num = nums[0]
        while i <= j:
            middle = int((i + j) / 2)
            if nums[middle] > min_num:
                i = middle + 1
            else:
                min_num = nums[middle]
                j = middle - 1

        return min_num

