class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}

        for value in nums:
            hash[value]=hash.get(value, 0)+1
#bucket sort create a list inside a list to keep the values we have to put the values 
#based on its count which is the index here. Thats why ewe need list inside list
        bucket=[[] for i in range(len(nums)+1)]

        for num, count in hash.items():
            bucket[count].append(num)
        res=[]
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
            

        



        