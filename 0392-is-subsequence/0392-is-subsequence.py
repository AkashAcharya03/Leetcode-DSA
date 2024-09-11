class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index=0
        count=0
        for i in range (0,len(s)):
            flag=0
            # print(s[i])
            for j in range(index,len(t)):
                print(s[i],t[j])
                if s[i]==t[j]:
                    index=j+1
                    flag=1
                    count+=1
                    break
            if flag==1:
                continue
            else:
                return False
        if count==len(s):
            return True
                
                
                    