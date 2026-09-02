class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left=0

        currentSum=0
        for right in range(len(nums)):
            currentSum+=nums[right]
            while currentSum>=target:
                mini=min(mini, right-left+1)
                currentSum-=nums[left]
                left+=1
        return 0 if mini==float('inf') else mini
                

            
            