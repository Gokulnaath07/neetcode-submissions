class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        hash={"}":"{", "]":"[", ")":"("}
        stack=[]
        for i in s:
            if i in hash:
                if stack and stack[-1]==hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        