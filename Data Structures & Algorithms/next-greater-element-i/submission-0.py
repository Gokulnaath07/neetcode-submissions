class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #monotonic stack

        stack=[]
        map={}
        res=[]
        for i in nums2:
            while stack and stack[-1]<i:
                map[stack.pop()]=i
            stack.append(i)
        for i in nums1:
            v=map.get(i,-1)
            res.append(v)
        return res
        