class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        i = 0
        result = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, n):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append([intervals[i][0], intervals[i][1]])
            
        return result