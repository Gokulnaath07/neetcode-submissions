from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts=defaultdict(list)
        for i in strs:
            count =[0]*26
            for s in i:
                count[ord(s)-ord('a')]+=1
            dicts[tuple(count)].append(i)
        return list(dicts.values())
            
        