class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map={}

        for i in nums:
            map[i]=map.get(i, 0)+1
        
        bucket=[[] for buck in range(len(nums)+1)]

        for v, i in map.items():
            bucket[i].append(v)
        res=[]
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res
                    break
        return []

        