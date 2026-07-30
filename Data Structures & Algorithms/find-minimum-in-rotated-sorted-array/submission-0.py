class Solution:
    def findMin(self, nums: List[int]) -> int:

        left=0
        right=len(nums)-1
        res=nums[0]

        while left<=right:
            if nums[right]>nums[left]:
                res=min(res, nums[left])
                break
            
            middle=(left+right)//2
            res=min(res, nums[middle])
            if nums[middle]>=nums[right]:
                left=middle+1
            else:
                right=middle-1
        return res
        