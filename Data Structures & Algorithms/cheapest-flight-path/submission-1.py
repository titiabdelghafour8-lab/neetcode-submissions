class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 1000000000

        d = [INF] * n
        d[src] = 0
        for i in range(k + 1):
            tmp = d.copy()
            flag = False
            for u, v, w in flights:
                if tmp[u] + w < d[v]:
                    d[v] = tmp[u] + w
                    flag = True
            if not flag:
                break
                    
        return d[dst] if d[dst] < INF else -1