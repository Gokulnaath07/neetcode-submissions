class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])

        # current=[intervals[0]]

        # for start, end in intervals:
        #     if start<=current[-1][1]:
        #         current[-1][1]=max(current[-1][1], end)
        #     else:
        #         current.append([start, end])
        # return current
        

        current=newInterval
        res=[]
        for i in intervals:
            if i[1]<current[0]:
                res.append(i)
            elif i[0]<=current[1]:
                current[0]=min(current[0], i[0])
                current[1]=max(current[1], i[1])
            else:
                res.append(current)
                current=i
        res.append(current)
        return res
                
                







