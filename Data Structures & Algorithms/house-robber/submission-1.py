class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0

        for n in nums:
            curr=max(prev2+n, prev1)
            prev2=prev1
            prev1=curr
        return prev1
        

        