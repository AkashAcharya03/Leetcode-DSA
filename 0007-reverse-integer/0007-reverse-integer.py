class Solution:
    def reverse(self, x: int) -> int:
        
        rev=0
        if x<0:
            new=x-x-x
            while(new!=0):
                rem=new%10

                rev=rev*10+rem

                new=new//10
            if -rev<=-(2**31) or -rev>=(2**31)-1:
                return 0
            return(-rev)
        else:
            new=x
            while(new!=0):
                rem=new%10

                rev=rev*10+rem

                new=new//10
            if rev<=-(2**31) or rev>=(2**31)-1:
                return 0
            return(rev)
