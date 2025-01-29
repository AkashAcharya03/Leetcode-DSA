class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        len1=len(a)
        len2=len(b)
        num1=a[::-1]
        num2=b[::-1]
        carry=0
        if len1>len2:
            num2=num2+str(0)*(len1-len2)
        else:
            num1=num1+str(0)*(len2-len1)
        for i in range (0,len(num1)):
            sum=int(num1[i])^int(num2[i])^carry
            sum1=int(num1[i])+int(num2[i])+carry
            carry=0
            if sum1>1:
                carry=1
            result.append(str(sum))
        if carry:
            result.append(str(1))
        answer=result[::-1]

        return(''.join(answer))

            

        