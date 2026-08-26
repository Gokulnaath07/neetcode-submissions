class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i]=hash.get(i, 0)+1
        for i, v in enumerate(s):
            if hash[v]==1:
                return i
        return -1
        