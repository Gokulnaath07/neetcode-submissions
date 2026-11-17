class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for tar in range(len(nums)):
            if tar>0 and nums[tar]==nums[tar-1]:
                continue
            left=tar+1
            right=len(nums)-1

            while left<right:
                val=nums[tar]+nums[left]+nums[right]
                if val<0:
                    left+=1
                elif val>0:
                    right-=1
                else:
                    res.append([nums[tar],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res
                


        
        
        