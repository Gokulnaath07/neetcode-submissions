class Solution:
    def maxArea(self, nums: List[int]) -> int:

        left=0
        right=len(nums)-1
        longest=0

        while left<right:
            area=(right-left)*min(nums[left], nums[right])
            longest=max(longest, area)
            if nums[left]<nums[right]:
                left+=1
            else:
                right-=1
        return longest
            
            
        