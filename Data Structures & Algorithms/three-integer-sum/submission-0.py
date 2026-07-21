class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for target in range(len(nums)):
            if target>0 and nums[target]==nums[target-1]:
                continue
            left=target+1
            right=len(nums)-1

            while left<right:

                if (nums[left]+nums[right])<-(nums[target]):
                    left+=1
                elif (nums[left]+nums[right])>-(nums[target]):
                    right-=1
                else:
                    res.append([nums[target], nums[left], nums[right]])
                    left+=1
                    
                    while left <right and nums[left]==nums[left-1]:
                        left+=1
        return res
                


            