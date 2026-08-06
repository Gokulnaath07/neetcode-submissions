#Input: strs = ["act","pots","tops","cat","stop","hat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashM=defaultdict(list)

        for i in strs:
            res=[0]*26
            for s in i:
                res[ord(s)-ord('a')]+=1
            hashM[tuple(res)].append(i)
        return list(hashM.values())



 
                

        