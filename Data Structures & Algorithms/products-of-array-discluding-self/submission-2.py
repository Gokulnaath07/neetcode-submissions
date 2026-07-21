class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

#set prefix and post fix to 1. We will have a new array 
#We set the prefix to the new array on that index
#we will be multiplying the prefix with the current value of given array

#We again use the created array and multiply the values with postfix from the backwards 
#when we update the value in array we then update postfix with the given array value which is also from backwards

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
        
        