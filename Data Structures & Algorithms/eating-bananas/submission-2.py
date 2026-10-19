import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_element = max(piles)
        n = len(piles)
        left = 1
        right = max(piles)
        k_min = 0
        while left <= right:
            k = int((right + left) / 2)
            hours_count = 0
            for i in range(n):
                hours_count += math.ceil(piles[i] / k)
            if hours_count <= h:
                k_min = k
                right = k - 1
            else:
                left = k + 1
           
        return k_min

