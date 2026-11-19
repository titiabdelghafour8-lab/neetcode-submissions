
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size  # Rank helps in balancing the tree
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    
    def same_set(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhatten(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j, manhatten(points[i], points[j])))
        edges.sort(key=lambda x: x[2])
        

        dsu = UnionFind(n)
        res = 0
        for i, j, cost in edges:
            if not (dsu.same_set(i, j)):
                res += cost
            dsu.union(i, j)
        return res