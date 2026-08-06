#nums=[1,2,3,4,5,6,2,2,5,3] val=2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
            



        