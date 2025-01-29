class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # k=0
        # for i in range(0,len(haystack)):
        #     if needle[k]==haystack[i]:
        #         if k==len(needle)-1:
        #             return i+1-len(needle)
        #         k+=1
        #     else:
        #         k=0
        # return -1                     
        for i in range(0,len(haystack)-len(needle)+1):
            if needle in haystack[i:i+len(needle)]:
                return (i)
        return (-1)
                
                