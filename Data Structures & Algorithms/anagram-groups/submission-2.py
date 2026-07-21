from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_num=defaultdict(list)
        
        for s in strs:
            arr=[0]*26
            for char in s:
                val=ord(char)-ord('a')
                arr[val]+=1
            dict_num[tuple(arr)].append(s)
        return list(dict_num.values())
            
        