strs=["act", "pops", "cat", "tac", "sopp", "lin", "nil"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash=defaultdict(list)

        for i in strs:
            arr=[0]*26
            for s in i:
                arr[ord(s)-ord('a')]+=1
            hash[tuple(arr)].append(i)
        return list(hash.values())
                

        