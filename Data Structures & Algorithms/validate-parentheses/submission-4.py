class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashMap={")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in hashMap:
                stack.append(c)
            else:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
        

        