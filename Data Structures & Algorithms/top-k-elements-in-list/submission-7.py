from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        #create bucket list
        bucket=[[] for _ in range(len(nums)+1)]

        #now add values in bucketbased on the frequency place the number in that 
        #index (which is the freq itself).
        for num, freq in count.items():
            bucket[freq].append(num)
        out=[]
        for i in range (len(bucket)-1,0,-1):
            for j in bucket[i]:
                out.append(j)
            if len(out)==k:
                return out