class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_s1=set(nums1)
        res=[]

        for i in nums2:
            if i in nums_s1:
                res.append(i)
                nums_s1.remove(i)
        return res

        
        