class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left=self.binary_search(nums, target, True)
        right=self.binary_search(nums, target, False)

        return [left, right]


    def binary_search(self, nums: List[int], target: int, leftBias:bool):
        l=0 
        r=len(nums)-1
        i=-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                i=m
                if leftBias:
                    r=m-1
                else:
                    l=m+1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return i

        