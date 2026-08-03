class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l =0
        r=len(heights)-1
        longest=0

        while l<r:
            area=(r-l)*min(heights[l], heights[r])
            longest=max(longest, area)
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1
        return longest

            