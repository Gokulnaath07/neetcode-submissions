class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            arr[i]=prefix
            prefix=prefix*nums[i]

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            arr[i]=arr[i]*postfix
            postfix=postfix*nums[i]
        
        return arr
        
        