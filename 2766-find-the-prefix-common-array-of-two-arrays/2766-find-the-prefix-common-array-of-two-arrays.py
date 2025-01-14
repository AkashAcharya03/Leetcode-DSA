class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer=[]
        for i in range(0,len(A)):
            count=0
            for j in range (0,i+1):
                for k in range(0,i+1):
                    if A[j]==B[k]:
                        count+=1
            
            answer.append(count)
        return(answer)