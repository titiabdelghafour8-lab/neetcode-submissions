
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_count_map: dict[int, int] = {}
        for num in nums:
            elements_count_map[num] = elements_count_map.get(num, 0) + 1
        L = sorted(elements_count_map.items(), key= lambda item: item[1], reverse=True)
        return [L[i][0] for i in range(k)]
        