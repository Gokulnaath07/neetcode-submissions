class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mapt=Counter(t)
        need=len(mapt)

        have=0
        window=defaultdict(int)

        left=0
        mini=float('inf')

        for right in range(len(s)):
            window[s[right]]+=1
            if s[right] in mapt and window[s[right]]==mapt[s[right]]:
                have+=1
            while need==have:
                if right-left+1<mini:
                    start=left
                    mini=right-left+1
                window[s[left]]-=1
                if s[left] in mapt and window[s[left]]<mapt[s[left]]:
                    have-=1
                left+=1
        if mini==float('inf'):
            return ""
        return s[start:start+mini]
            
        