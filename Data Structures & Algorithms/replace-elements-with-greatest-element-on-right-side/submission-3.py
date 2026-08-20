class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        last=-1
        ans=[0]*len(arr)

        for i in range(len(arr)-1, -1, -1):
            ans[i]=last
            last=max(last, arr[i])
        return ans
            
        