import heapq
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_list = []
        window = []
        removed = Counter()
        for i in range(k):
            heapq.heappush(window, -nums[i])
        right = k - 1 
        while right + 1 < n:
            while window and -window[0] in removed and removed[-window[0]] > 0:
                removed[-window[0]] -= 1
                heapq.heappop(window)
                
            max_list.append(-window[0])
            heapq.heappush(window, -nums[right + 1])
            removed[nums[right - k + 1]] = removed.get(nums[right - k + 1], 0) + 1
            right += 1
        
        while window and -window[0] in removed and removed[-window[0]] > 0:
            removed[-window[0]] -= 1
            heapq.heappop(window)
        if window:
            max_list.append(-window[0])
        return max_list
