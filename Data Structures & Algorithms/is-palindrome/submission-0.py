class Solution:
    def isPalindrome(self, s: str) -> bool:

        stri=" ".join(c.lower() for c in s if c.isalnum())
        left =0
        right=len(stri)-1

        while left<right:
            if stri[left] != stri[right]:
                return False
            left+=1
            right-=1
        return True