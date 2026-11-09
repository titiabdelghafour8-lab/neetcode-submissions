class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        n = len(intervals)
        result = [[intervals[0][0], intervals[0][1]]]
        count = 0
        for i in range(1, n):
            if result[-1][1] > intervals[i][0]:
                count += 1
                continue
                
            result.append([intervals[i][0], intervals[i][1]])
        return count

