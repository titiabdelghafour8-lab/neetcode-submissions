import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(points[i][0]**2 + points[i][1]**2, i) for i in range(len(points))]
        heapq.heapify(distances)
        k_closest = []
        while len(distances) > len(points) - k:
            k_closest.append(points[heapq.heappop(distances)[1]])
        return k_closest
            
