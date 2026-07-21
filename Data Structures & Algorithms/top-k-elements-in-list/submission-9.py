class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        hash={}
        for i in nums:
            hash[i]=hash.get(i, 0)+1

        bucket=[[] for i in range(len(nums)+1)]

        for val, index in hash.items():
            bucket[index].append(val)

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
        


        
            