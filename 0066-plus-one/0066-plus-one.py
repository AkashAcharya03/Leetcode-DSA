class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        result=[]
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:

                sum=digits[i]+1+carry
                carry=0
                print("vjbbdv")
            else:
                sum=digits[i]+carry
                carry=0
            if sum>9:
                print("vjbbdv")

                carry=sum//10
                result.append(sum%10)
            else:
                result.append(sum)
        if carry:
            result.append(1)


        return(result[::-1])



        