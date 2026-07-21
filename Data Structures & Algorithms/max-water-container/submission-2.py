class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        heightest=0
        while left < right:
            val=(right-left)*min(heights[right], heights[left])
            heightest=max(heightest, val)
            if heights[left]< heights[right]:
                left+=1

            else:
                right-=1

        return heightest
            
            
        