class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i in range(len(nums)):
            ans_val=target-nums[i]
            if ans_val not in hashmap: 
                hashmap[nums[i]]=i
            else:
                return [hashmap[ans_val], i ]
        