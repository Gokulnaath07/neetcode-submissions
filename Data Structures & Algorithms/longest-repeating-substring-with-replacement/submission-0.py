from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count=defaultdict(int)
        left=0
        res=0

        for right in range(len(s)):

            #we have to check the substring with the 
            #most occured count alphabet from the given string

            #frequency of the input
            count[s[right]]+=1

            while (right-left+1)-max(count.values()) >k:
                count[s[left]]-=1
                left+=1
            res=max(res, right-left+1)
        return res