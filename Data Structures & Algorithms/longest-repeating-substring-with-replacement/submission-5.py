class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map=defaultdict(int)
        left=0
        longest=0
        maxF=0

        for right in range(len(s)):
            map[s[right]]+=1
            maxF=max(maxF, map[s[right]])
            if (right-left+1)-maxF>k:
                map[s[left]]-=1
                left+=1
            longest=max(longest, right-left+1)
        return longest

        
        