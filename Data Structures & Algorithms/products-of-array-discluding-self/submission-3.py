class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

#set prefix and post fix to 1. We will have a new array 
#We set the prefix to the new array on that index
#we will be multiplying the prefix with the current value of given array

#We again use the created array and multiply the values with postfix from the backwards 
#when we update the value in array we then update postfix with the given array value which is also from backwards

        prefix=1
        arr=[1]*len(nums)

        for i in range(len(nums)):
            arr[i]=prefix
            prefix*=nums[i]
        
        suffix=1
        for i in range(len(nums)-1, -1, -1):
            arr[i]=suffix*arr[i]
            suffix*=nums[i]

        return arr