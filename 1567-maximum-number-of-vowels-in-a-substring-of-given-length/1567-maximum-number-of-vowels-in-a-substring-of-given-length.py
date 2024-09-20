class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # maxcount=0
        # for i in range (0,len(s)-k+1):
        #     count=0
        #     for j in s[i:i+k]:
        #         if j in 'aeiou':
        #             count+=1
        #             maxcount=max(count,maxcount)
        # return maxcount
                

        vowels = 'aeiou'
        maxcount = 0
        count = 0
        
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxcount = count
        
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            
            maxcount = max(maxcount, count)
        
        return maxcount

