#Input: strs = ["act","pots","tops","cat","stop","hat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)

        for word in strs:
            arr=[0]*26
            for s in word:
                arr[ord(s)-ord('a')]+=1
            map[(tuple(arr))].append(word)
        return list(map.values())


        