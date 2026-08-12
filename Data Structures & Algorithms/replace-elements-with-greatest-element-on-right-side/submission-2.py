class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        rep=-1
        

        for i in range(len(arr)-1, -1, -1):
            temp=arr[i]
            arr[i]=rep
            rep=max(rep, temp)
        return arr
            


        