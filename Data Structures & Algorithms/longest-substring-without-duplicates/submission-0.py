class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        length=0
        num_set=set()

        for right in range(len(s)):
            
            while s[right] in num_set:
                num_set.remove(s[left])
                left+=1
            
            num_set.add(s[right])
            length=max(length, right-left+1)
        return length
        