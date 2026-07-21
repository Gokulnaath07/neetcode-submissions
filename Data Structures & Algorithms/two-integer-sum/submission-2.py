class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i, val in enumerate(nums):
            current=target-val
            if current in hash:
                return [hash[current], i]
            hash[val]=i
        return []

            
             

        