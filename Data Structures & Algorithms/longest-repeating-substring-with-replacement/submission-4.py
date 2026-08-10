class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hash=defaultdict(int)

        left =0
        maxF,longest=0, 0
        for right in range(len(s)):
            hash[s[right]]+=1
            maxF=max(maxF, hash[s[right]])

            if (right-left+1)-maxF>k:
                hash[s[left]]-=1
                left+=1
            longest=max(longest, right-left+1)
        return longest



