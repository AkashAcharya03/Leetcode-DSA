class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack=[]
        for i in s:
            if i in dic.keys():
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)
        return not stack
