class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlaps = []
        heapq.heapify(overlaps)
        for interval in intervals:
            if overlaps and overlaps[0] < interval[0]:
              heapq.heappop(overlaps)
            heapq.heappush(overlaps, interval[1])
        return len(overlaps)
