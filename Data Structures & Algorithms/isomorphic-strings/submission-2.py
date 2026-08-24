class Solution:
    def helper(self, s: str, t: str)->bool:
        map={}

        for i in range(len(s)):
            if s[i] in map and map[s[i]]!=t[i]:
                return False
            map[s[i]]=t[i]
        return True
    
    def isIsomorphic(self, s: str, t: str)->bool:
        return self.helper(s, t) and self.helper(t, s)