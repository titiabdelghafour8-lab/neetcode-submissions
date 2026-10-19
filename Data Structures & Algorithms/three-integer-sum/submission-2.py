class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        L = set()
        for k in range(n):
            i = 0 if k != 0 else 1
            j = n - 1 if k != n-1 else n - 2
            while i < j:
                if i == k:
                    i += 1
                    continue
                if j == k:
                    j -= 1
                    continue
                if nums[i] + nums[j] == -nums[k]:
                    L.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > -nums[k]:
                    j -= 1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
        return [list(triplet) for triplet in L]
            