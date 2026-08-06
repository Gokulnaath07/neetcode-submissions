nums=[-4,-2,0,1,2,3]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums
        