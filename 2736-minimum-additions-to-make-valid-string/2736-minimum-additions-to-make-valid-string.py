class Solution:
    def addMinimum(self, word: str) -> int:
        stack = list(word)
        count = 0
        while stack:
            if stack and stack[-1] == "c":
                stack.pop()
            else:
                count += 1

            if stack and stack[-1] == "b":
                stack.pop()
            else:
                count += 1

            if stack and stack[-1] == "a":
                stack.pop()
            else:
                count += 1
            

        return(count)
