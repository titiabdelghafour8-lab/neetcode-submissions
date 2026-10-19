import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        sorted_l = []
        copy = self.nums.copy()
        for i in range(self.k):
            sorted_l.append(heapq.heappop(copy))
        return -sorted_l[-1]

        
