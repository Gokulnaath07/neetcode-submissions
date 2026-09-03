class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Input: piles = [1,4,3,2], h = 9
        left=1
        right=max(piles)
        res=0

        while left<=right:
            m=(left+right)//2
            totalHours=0
            for p in piles:
                totalHours+=math.ceil(float(p)/m)
            if totalHours>h:
                left=m+1
            else:
                res=m
                right=m-1
        return res
                
            
        

                    
                    



        