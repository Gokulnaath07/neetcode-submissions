class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        mapf=Counter(tasks)

        maxFval=max(mapf.values())
        countMaxFVal=0
        for i in mapf.values():
            if i==maxFval:
                countMaxFVal+=1
        return max(len(tasks), (maxFval-1)*(n+1)+countMaxFVal)
        