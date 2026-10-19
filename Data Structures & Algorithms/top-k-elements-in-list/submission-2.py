class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in count_map.items():
            freq_buckets[count].append(num)
            
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result