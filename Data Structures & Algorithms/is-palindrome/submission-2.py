class Solution:
    def isPalindrome(self, s: str) -> bool:

        stri=" ".join(c.lower() for c in s if c.isalnum())
        right=len(stri)-1
        left=0

        while right>left:
            if stri[right] != stri[left]:
                return False
            right-=1
            left+=1
        return True