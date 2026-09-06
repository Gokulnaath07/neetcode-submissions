class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        length=0
        set_s=set()

        for right in range(len(s)):

            while s[right] in set_s:
                set_s.remove(s[left])
                left+=1

            set_s.add(s[right])   
            length=max(length, right-left+1)
        return length     