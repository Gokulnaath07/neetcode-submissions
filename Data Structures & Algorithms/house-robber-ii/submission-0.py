class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def rob(nums:List[int]):
            prev1=0
            prev2=0

            for n in nums:
                curr=max(prev1, prev2+n)
                prev2=prev1
                prev1=curr
            return prev1
        
        return max(rob(nums[1:]), rob(nums[:-1]))
                

        