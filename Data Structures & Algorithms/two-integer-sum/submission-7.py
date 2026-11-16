class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}
        for i, v in enumerate(nums):
            curr=target-v
            if curr in hash:
                return [hash[curr], i]
            hash[v]=i
        


        