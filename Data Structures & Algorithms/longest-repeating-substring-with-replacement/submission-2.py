from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash=defaultdict(int)          
        
        

        left=0
        res=0
        maxF=0

        for right in range(len(s)):
            hash[s[right]]+=1
            maxF=max(maxF, hash[s[right]])

            while (right-left+1)-maxF>k:
                hash[s[left]]-=1
                left+=1
            res=max(res, right-left+1)
        return res


            


            