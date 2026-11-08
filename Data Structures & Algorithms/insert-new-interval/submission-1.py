class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        result = []
        n = len(intervals)
        i = 0
        while i < n: 
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
                continue
            while i < n and intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                flag = True
                i += 1
            result.append([newInterval[0], newInterval[1]])
            break
        while i < n:
            result.append(intervals[i])
            i += 1
        if newInterval[0] > intervals[n - 1][1]:
            result.append(newInterval)
        return result
            
            
                
