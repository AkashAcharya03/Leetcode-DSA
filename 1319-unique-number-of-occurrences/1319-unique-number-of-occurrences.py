class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in range(0,len(arr)):
            if arr[i] not in dic:
                dic[arr[i]]=1
            else:
                dic[arr[i]]+=1
        length=len(list(dic.values()))
        length1=len(set(list(dic.values())))
        return(length1==length)
        