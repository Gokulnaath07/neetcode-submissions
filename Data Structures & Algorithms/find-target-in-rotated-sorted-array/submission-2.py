class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        while left<right:
            m=(left+right)//2
            if nums[m]>nums[right]:
                left+=1
            else:
                right=m
        pivot=left

        # l=0
        # r=len(nums)-1

        # if target>=nums[pivot] and target<=nums[r]:
        #     l=pivot
        # else:
        #     r=pivot-1

        # while l<=r:
        #     m=(l+r)//2
        #     if nums[m]>target:
        #         r=m-1
        #     elif nums[m]==target:
        #         return m
        #     else:
        #         l=m+1
        # return -1

        def binarySearch(left: int, right: int)->int:
            while left<=right:
                m=(left+right)//2
                if target==nums[m]:
                    return m
                elif target<nums[m]:
                    right=m-1
                else:
                    left=m+1
            return -1
        
        res=binarySearch(pivot, len(nums)-1)
        if res!=-1:
            return res
        return binarySearch(0, pivot-1)




        