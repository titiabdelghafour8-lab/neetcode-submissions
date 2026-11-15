import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        m = len(intervals)
        n = len(queries)
        sorted_queries = [(queries[i], i) for i in range(n)]
        sorted_queries.sort()
        res = [-1] * n
        i = 0
        heap = []
        for q, idx in sorted_queries:
            while i < m and q >= intervals[i][0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while heap and q > heap[0][1]:
                heapq.heappop(heap)[0]

            if not heap:
                continue
            else:
                res[idx] = heap[0][0]
                

        return res
        