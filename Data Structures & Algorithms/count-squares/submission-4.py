from collections import defaultdict


class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)        
        self.xs = defaultdict(set)
        self.visited = set()

    def add(self, point: List[int]) -> None:
        self.counts[(point[0], point[1])] += 1
        self.xs[point[0]].add((point[0], point[1]))
        self.visited.add((point[0], point[1]))


    def count(self, point: List[int]) -> int:
        
        x, y = point
        if (x, y) not in self.visited:
            self.counts[(x, y)] += 1
        square_count = 0
        for _, py in self.xs[x]:
            d = abs(y - py)
            if d == 0:
                continue
            for alpha in (x + d, x - d):
                square_count += self.counts[(x, y)] * self.counts[(x, py)] * self.counts[(alpha, y)] * self.counts[(alpha, py)]
        if (x, y) not in self.visited:
            self.counts[(x, y)] -= 1
        return square_count

        

