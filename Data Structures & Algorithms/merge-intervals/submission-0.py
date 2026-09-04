class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        current=[intervals[0]]

        for start, end in intervals:
            lastend=current[-1][1]
            if lastend>=start:
                current[-1][1]=max(lastend, end)
            else:
                current.append([start, end])
        return current


                
        