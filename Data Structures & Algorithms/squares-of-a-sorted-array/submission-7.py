nums=[-4,-2,0,1,2,3]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # for i in range(len(nums)):
        #     nums[i]=nums[i]*nums[i]
        # nums.sort()
        # return nums

        left=0
        right=len(nums)-1
        res=[]

        while left<=right:
            if nums[right]*nums[right] <(nums[left]*nums[left]):
                res.append(nums[left]*nums[left])
                left+=1
            else:
                res.append(nums[right]*nums[right])
                right-=1
        return res[::-1]

        