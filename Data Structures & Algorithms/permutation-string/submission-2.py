class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        s1count={}
        windowhash={}

        for i in range(len(s1)):
            s1count[s1[i]]=s1count.get(s1[i],0)+1

        left =0

        have=0
        need=len(s1count)

        for right in range(len(s2)):
            rightC=s2[right]

            windowhash[rightC]=windowhash.get(rightC, 0)+1
            if rightC in s1count:
                if windowhash[rightC]==s1count[rightC]:
                    have+=1
                elif windowhash[rightC]==s1count[rightC]+1:
                    have-=1
            

            if (right-left+1)>len(s1):

                leftC=s2[left]
                if leftC in s1count:
                    if windowhash[leftC]==s1count[leftC]:
                        have-=1
                    elif windowhash[leftC] == s1count[leftC]+1:
                        have+=1

                windowhash[leftC]-=1
                left+=1

            if have==need:
                return True
        return False
        