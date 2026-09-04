class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        current=intervals[0]
        result=[]

        for interval in intervals:
            if interval[0]<=current[1]:
                current[1]=max(interval[1], current[1])
            else:
                result.append(current)
                current=interval
        result.append(current)#this is for the last value 
        return result

                
        