class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        left=0
        right=len(height)-1
        

        while left<right:
            
            if height[left]<height[right]:
                area=(right-left)*height[left]
                left+=1
            else:
                area=(right-left)*height[right]
                right-=1
            res=max(area, res)
        return res


        


        