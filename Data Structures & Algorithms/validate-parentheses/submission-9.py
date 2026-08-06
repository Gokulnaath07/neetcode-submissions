class Solution:
    def isValid(self, s: str) -> bool:
        
        hash={"}":"{", "]":"[", ")":"("}
        stack=[]

        for i in range(len(s)):

            if s[i] in hash:
                if stack and stack[-1] ==hash[s[i]]:
                    stack.pop()
                else:
                    return False
            else:

                stack.append(s[i])
        return True if not stack else False

       