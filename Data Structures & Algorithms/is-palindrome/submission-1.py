class Solution:
    def isPalindrome(self, s: str) -> bool:

        stri=" ".join(c.lower() for c in s if c.isalnum())
        return stri==stri[::-1]