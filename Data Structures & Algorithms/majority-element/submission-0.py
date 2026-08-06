class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashM={}
        longest=0

        for i in nums:
            hashM[i]=hashM.get(i, 0)+1
        for val, count in hashM.items():
            if count>len(nums)/2:
                return val
        
        
        