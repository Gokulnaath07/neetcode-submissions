class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #greedy approach. This is choosing one operation cares about current and goes with it

        intervals.sort(key=lambda c: c[1])
        prevEnd=intervals[0][1]

        remove=0

        for i in range(1, len(intervals)):
            if intervals[i][0]<prevEnd:
                remove+=1
            else:
                prevEnd=intervals[i][1]
        return remove


        