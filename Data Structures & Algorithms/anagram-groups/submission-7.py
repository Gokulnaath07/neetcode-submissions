class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)

        for word in strs:
            arr=[0]*26
            for i in word:
                arr[(ord(i)-ord('a'))]+=1
            hash[tuple(arr)].append(word)
        return list(hash.values())
                
        