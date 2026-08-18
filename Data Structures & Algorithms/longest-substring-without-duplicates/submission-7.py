class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets=set()

        left, longest=0, 0

        for right in range(len(s)):
            while s[right] in sets:
                sets.remove(s[left])
                left+=1
            sets.add(s[right])
            longest=max(longest, right-left+1)
        return longest



