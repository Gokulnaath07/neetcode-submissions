class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map={0:1}
        currSum=0
        count=0
        for num in nums:
            currSum+=num
            prefixSum=currSum-k

            count+=map.get(prefixSum, 0)

            map[currSum]=map.get(currSum, 0)+1
        
        return count


        