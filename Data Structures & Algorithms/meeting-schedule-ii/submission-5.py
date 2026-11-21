"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_interval = sorted(intervals, key = lambda x : x.start)
        d = 0
        min_heap = []
        schedule = {}
        for interval in sorted_interval:
            if min_heap and min_heap[0][0] <= interval.start:
                _, k = heapq.heappop(min_heap)
                schedule[k].append(interval)
                heapq.heappush(min_heap, (interval.end, k))
            else:
                d += 1
                k = d
                schedule[k] = [interval]
                heapq.heappush(min_heap, (interval.end, k))
        return d