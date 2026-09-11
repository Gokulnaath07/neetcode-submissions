class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #greedy approach. This is choosing one operation cares about current and goes with it

        intervals.sort(key=lambda c: c[1])
        remove=0
        pos=intervals[0][1]
        for start, end in intervals[1:]:
            if pos>start:
                remove+=1
            else:
                pos=end
        return remove