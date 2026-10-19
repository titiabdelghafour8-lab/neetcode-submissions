import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        rev_stones = [-stones[i] for i in range(len(stones))]
        heapq.heapify(rev_stones)
        while len(rev_stones) > 1:
            first_rock = heapq.heappop(rev_stones)
            second_rock = heapq.heappop(rev_stones) if rev_stones else 0
            if second_rock == 0:
                return first_rock 
            elif first_rock == second_rock:
                continue
            else:
                heapq.heappush(rev_stones, first_rock - second_rock)
        return -rev_stones[0] if rev_stones else 0
        