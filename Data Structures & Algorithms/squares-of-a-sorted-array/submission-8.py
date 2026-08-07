nums=[-4,-2,0,1,2,3]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        right=len(nums)-1
        left=0
        res=[]
        while left<=right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                res.append(nums[right]*nums[right])
                right-=1
            else:
                res.append(nums[left]*nums[left])
                left+=1
        return res[::-1]

        