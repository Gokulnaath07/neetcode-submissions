class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash={}
        for i in nums:
            hash[i]=hash.get(i, 0)+1
        for val, count in hash.items():
            if count>len(nums)/2:
                return val



            
        
        