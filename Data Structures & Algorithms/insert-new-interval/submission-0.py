class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])

        current=[intervals[0]]

        for start, end in intervals:
            if start<=current[-1][1]:
                current[-1][1]=max(current[-1][1], end)
            else:
                current.append([start, end])
        return current
        