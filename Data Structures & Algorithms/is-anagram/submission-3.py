class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s=set(s)
        sort_t=set(t)

        return Counter(s)==Counter(t)


        