from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for ticket in tickets:
            heapq.heappush(adj[ticket[0]], ticket[1])
            
        
        not_finished = ["JFK"]
        res = []
        while not_finished:
            el = not_finished[-1]
            if adj[el]:
                not_finished.append(heapq.heappop(adj[el]))
            else:
                res.append(not_finished.pop())
        
        return res[::-1]
                
            
                
