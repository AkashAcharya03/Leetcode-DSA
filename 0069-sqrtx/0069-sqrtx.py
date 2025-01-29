class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x==1:
            return 1
        sqr=1
        for i in range(2,x+1):
            if sqr<x and i*i>x:
                return(sqr)
            sqr=i



        