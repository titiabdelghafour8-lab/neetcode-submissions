"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
the idea behind this is: we always allocate room for guests and always free room for leavers, but we need to keep track of the order so we do check if: current comer < current leaver, to make sure it happens correctly, we allocate rooms before freeing them.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        max_available = 0
        rooms = 0
        n = len(intervals)
        starts = [c.start for c in intervals]
        ends = [c.end for c in intervals]
        starts.sort()
        ends.sort()
        i = 0
        j = 0
        while i < n:
            if starts[i] < ends[j]:
                rooms += 1 
                i += 1
            else:
                rooms -= 1
                j += 1
            max_available = max(max_available, rooms)
        return max_available
