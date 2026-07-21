from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_num=Counter(nums)
        new_list=[[] for _ in range(len(nums)+1)]
        for num, freq in heap_num.items():
            new_list[freq].append(num)
        
        out=[]
        for i in range(len(new_list)-1, 0, -1):
            for num in new_list[i]:
                out.append(num)
            if len(out)==k:
                return out
        
        
        