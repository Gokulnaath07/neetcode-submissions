class Solution:

    # def binary_search(self, l: int, r: int, nums: list[int], target: int)-> int:

    #     if l>r:
    #         return -1
    #     m=(l+r)//2

    #     if nums[m]==target:
    #         return m
    #     if nums[m]<target:
    #         return self.binary_search(m+1, r, nums, target)
    #     else:
    #         return self.binary_search(l, m-1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        # return self.binary_search(0, len(nums)-1, nums, target)
        l=0
        r=len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return -1




