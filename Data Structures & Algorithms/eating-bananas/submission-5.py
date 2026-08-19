class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Input: piles = [1,4,3,2], h = 9
        l=1 
        r=max(piles)
        res=r
        
        while l<=r:
            k=(l+r)//2
            totalHours=0
            for p in piles:
                totalHours+=math.ceil(float(p)/k)
            if totalHours>h:
                l=k+1
            else:
                res=k
                r=k-1
        return res




        