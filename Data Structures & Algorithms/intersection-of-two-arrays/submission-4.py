class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_s=set(nums1)
        res=set()

        # for i in range(len(nums2)):
        #     if nums2[i] in nums_s:
        #         res.add(nums2[i])
        return list(set(nums1)& set(nums2))




