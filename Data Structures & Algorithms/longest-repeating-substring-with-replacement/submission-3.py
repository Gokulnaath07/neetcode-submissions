from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        longest=0
        maxF=0
        hash={}

        for right in range(len(s)):
            hash[s[right]]=hash.get(s[right],0)+1
            maxF=max(maxF, hash[s[right]])

            while (right-left+1)-maxF>k:
                hash[s[left]]-=1
                left+=1
            longest=max(longest, right-left+1)
        return longest
                


            