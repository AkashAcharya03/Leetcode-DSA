class Solution:
    def reverseVowels(self, s: str) -> str:
        new=''
        new2=''
        count=0
        # count2=0
        for i in range (0,len(s)):
            if s[i]=='a' or  s[i]=='A' or s[i]=='e' or  s[i]=='E' or s[i]=='i' or  s[i]=='I' or s[i]=='o' or  s[i]=='O' or s[i]=='u' or  s[i]=='U':
                new+=s[i]
        reversed=new[::-1]
        for i in range (0,len(s)):
            if s[i]=='a' or  s[i]=='A' or s[i]=='e' or  s[i]=='E' or s[i]=='i' or  s[i]=='I' or s[i]=='o' or  s[i]=='O' or s[i]=='u' or  s[i]=='U':
                new2+=reversed[count]
                count+=1
            else:
                new2+=s[i]
        return new2

