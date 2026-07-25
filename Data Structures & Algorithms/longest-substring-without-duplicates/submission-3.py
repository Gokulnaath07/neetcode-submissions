class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_S=set()
        left=0
        maxi=0

        for right in range(len(s)):
            while s[right] in hash_S:
                hash_S.remove(s[left])
                left+=1
            hash_S.add(s[right])
            maxi=max(maxi, right-left+1)
        return maxi
            