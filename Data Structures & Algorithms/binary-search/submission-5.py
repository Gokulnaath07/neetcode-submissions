class Solution:

    def search(self, nums:list[int], target: int)-> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            if nums[m]>target:
                r=m-1
            if nums[m]<target:
                l=m+1
            
        return -1






























    # # def binary_search(self, l: int, r: int, nums: list[int], target: int)-> int:

    # #     if l>r:
    # #         return -1
    # #     m=(l+r)//2

    # #     if nums[m]==target:
    # #         return m
    # #     if nums[m]<target:
    # #         return self.binary_search(m+1, r, nums, target)
    # #     else:
    # #         return self.binary_search(l, m-1, nums, target)

    # def search(self, nums: List[int], target: int) -> int:
    #     # return self.binary_search(0, len(nums)-1, nums, target)
    #     l=0
    #     r=len(nums)-1

    #     while l<=r:
    #         mid=(l+r)//2
    #         if nums[mid]==target:
    #             return mid
    #         if nums[mid]>target:
    #             r=mid-1
    #         if nums[mid]<target:
    #             l=mid+1
    #     return -1











