class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times_dict = defaultdict(list)
        for el in times:
            times_dict[el[0] - 1].append((el[1] - 1, el[2]))
        INF = 100000
        marked = [False] * n
        min_dist = [INF] * n
        min_dist[k - 1] = 0
        res = 0
        for i in range(n):
            v = -1
            for j in range(n):
                if (not marked[j]) and (v == -1 or min_dist[j] <= min_dist[v]):
                    v = j 
            if min_dist[v] == INF:
                return -1
            marked[v] = True
            res = max(res, min_dist[v])
            for el in times_dict[v]:
                if min_dist[el[0]] > (min_dist[v] + el[1]):
                    min_dist[el[0]] = min_dist[v] + el[1]
        return res
                    
            


                    
