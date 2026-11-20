class Solution:
    def maxArea(self, nums: List[int]) -> int:

        left=0
        right=len(nums)-1
        maxi=0

        while right >left:
            area=(right-left)*min(nums[left], nums[right])
            maxi=max(area, maxi)
            if nums[left]>nums[right]:
                right-=1
            else :
                left+=1
        return maxi
            
            
        