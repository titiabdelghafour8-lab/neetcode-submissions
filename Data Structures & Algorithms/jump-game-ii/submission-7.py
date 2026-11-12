class Solution:
    def jump(self, nums: List[int]) -> int:
            def max_and_idx(arr):
                max_el = arr[0] + 1
                idx = 0
                for i in range(len(arr)):
                    if max_el <= (arr[i] + i + 1):
                        idx = i
                        max_el = arr[i] + i + 1
                return (idx, max_el)

            n = len(nums)
            i = 0
            res = 0
            while i < n - 1:
                if nums[i] >= n - 1:
                    return (res + 1)
                idx, best_candidate = max_and_idx(nums[i + 1: nums[i] + i + 1])
                
                if (i + nums[i]) >= n - 1:
                    return res + 1


                if nums[i] < best_candidate:
                    if best_candidate >= n - 1:
                        return res + 2
                    i += (idx + 1)
                    
                else:
                    i += nums[i]
                    if i >= n - 1:
                        return res + 1

                res += 1
            
            
            return res