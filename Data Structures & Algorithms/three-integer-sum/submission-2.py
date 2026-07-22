class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for target in range(len(nums)):
            #here we are skipping 0th index 
            #because if we do 0-1 the its -1 
            #then we will be comparing last number to first which is wrong
            if target>0 and nums[target]==nums[target-1]:
                continue
            
            left=target+1
            right = len(nums)-1

            while left<right:
                if nums[left]+nums[right]+nums[target]<0:
                    left+=1
                elif nums[left]+nums[right]+nums[target]>0:
                    right-=1
                else:
                    res.append([nums[left],nums[right],nums[target]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res
            
            