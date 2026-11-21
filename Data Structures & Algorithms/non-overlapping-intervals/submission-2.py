class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_jobs = sorted(intervals, key = lambda x: x[1])
        S = []
        last_finish_time = float('-inf')
        for interval in sorted_jobs:
            start_time, finish_time = interval
            if start_time >= last_finish_time:
                S.append(interval)
                last_finish_time = finish_time
        return len(intervals) - len(S)