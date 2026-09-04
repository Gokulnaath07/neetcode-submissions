"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #output=2
        #[0,40]
        #([5,10][15,20])

        #min heap
        if not intervals:
            return 0
        heap=[]
        intervals.sort(key=lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            start=interval.start
            end = interval.end
            if heap[0]<=start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)



            



        

        


        