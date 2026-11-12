

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def max_and_idx(arr):
            if not arr:
                return (0, 0)
            max_el = arr[0]
            idx = 0
            for i in range(len(arr)):
                if max_el <= arr[i]:
                    idx = i
                    max_el = arr[i]
            return (idx, max_el)

        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == 0:
                return False
            if nums[i] >= n - 1:
                return True
            idx, best_candidate = max_and_idx(nums[i + 1: nums[i] + i + 1])
            indirect_jump = best_candidate + (idx + 1)
            if nums[i] < indirect_jump:
                i += (idx + 1)
            else:
                i += nums[i]
        if i >= (n - 1):
            return True
        return False

        