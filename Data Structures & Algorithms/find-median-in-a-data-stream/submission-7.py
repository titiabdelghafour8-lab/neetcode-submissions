import heapq

class MedianFinder:
    
    def __init__(self):
        self.lowerOnes = []
        self.upperOnes = []
    def addNum(self, num: int) -> None:
        if not self.upperOnes or num >= self.upperOnes[0]:
            heapq.heappush(self.upperOnes, num)
        else:
            heapq.heappush(self.lowerOnes, -num)
        if len(self.lowerOnes) > (len(self.upperOnes) + 1):
            heapq.heappush(self.upperOnes, -heapq.heappop(self.lowerOnes))
        elif len(self.upperOnes) > (len(self.lowerOnes) + 1):
            heapq.heappush(self.lowerOnes, -heapq.heappop(self.upperOnes))


    def findMedian(self) -> float:
        if len(self.lowerOnes) < len(self.upperOnes):
                return self.upperOnes[0]
        elif len(self.lowerOnes) > len(self.upperOnes):
            return -self.lowerOnes[0]
        else:
            return (self.upperOnes[0] - self.lowerOnes[0]) / 2
        
        