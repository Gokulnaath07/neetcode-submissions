class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char=len(s)-1
        length=0

        while s[char]==' ':
            char-=1
        while char>=0 and s[char]!= ' ':
            char-=1
            length+=1
        return length
                

        
        