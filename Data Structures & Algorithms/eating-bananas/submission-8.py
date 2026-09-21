class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left=1
        right=max(piles)

        while left<=right:
            mid=(left+right)//2
            totalhours=0
            for p in piles:
                totalhours+=math.ceil(float(p)/mid)
            if totalhours>h:
                left=mid+1
            else:
                right=mid-1
        return left
            
                
            
        

                    
                    



        