class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            # num=list(str(x))
            # num1=''.join(num[1:])
            # x=int(num1)
            return False
        n=x
        rev=0
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        if rev==x:
            return True
        else:
            return False
        