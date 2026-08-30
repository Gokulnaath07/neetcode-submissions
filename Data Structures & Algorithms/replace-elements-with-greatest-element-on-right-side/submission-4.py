class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix=-1
        res=[0]*len(arr)

        for i in range(len(arr)-1, -1, -1):
            res[i]=suffix
            suffix=max(suffix, arr[i])
        return res





        
            
        