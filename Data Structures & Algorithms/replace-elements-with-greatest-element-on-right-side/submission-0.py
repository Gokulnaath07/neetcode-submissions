class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        rep=-1
        ans=[0]*len(arr)

        for i in range(len(arr)-1, -1, -1):
            ans[i]=rep
            rep=max(rep, arr[i])
        return ans
            


        