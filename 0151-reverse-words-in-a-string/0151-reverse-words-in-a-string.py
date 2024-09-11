class Solution:
    def reverseWords(self, s: str) -> str:
        while True:
            if '  ' in s:
                s=s.replace('  ',' ')
            else:
                break
        print(s)
        
        countf=0
        countl=len(s)
        for i in range(0,len(s)):
            if s[i]==' ':
                countf=i+1
            else:
                break
        for i in range(len(s)-1,0,-1):
            if s[i]==' ':
                countl-=1
            else:
                break

        aaa=s[countf:countl]
        new=aaa.split(' ')
        
        
        reverse=new[::-1]
        return ' '.join(reverse)
        