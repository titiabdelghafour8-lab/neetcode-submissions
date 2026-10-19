
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_count_map: dict[int, int] = {}
        for num in nums:
            if num in elements_count_map:
                elements_count_map[num] += 1
            if num not in elements_count_map:
                elements_count_map[num] = 1
        L = sorted(elements_count_map.items(), key= lambda item: item[1], reverse=True)
        return [L[i][0] for i in range(k)]
        