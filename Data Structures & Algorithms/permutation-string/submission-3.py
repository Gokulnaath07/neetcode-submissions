class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps1=Counter(s1)
        maps2=defaultdict(int)

        n=len(s1)

        left=0
        
        for right in range(len(s2)):
            maps2[s2[right]]+=1
            if (right-left+1)>len(s1):
                maps2[s2[left]]-=1
                if maps2[s2[left]]==0:
                    del maps2[s2[left]]
                left+=1
            if maps2==maps1:
                return True
        return False

        
        