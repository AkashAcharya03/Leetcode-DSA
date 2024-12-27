class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        dic1={}
        dic2={}
        for i in range(0,len(word1)):
            if word1[i] not in dic1:
                dic1[word1[i]]=1
            else:
                dic1[word1[i]]+=1
        
        for i in range(0,len(word2)):
            if word2[i] not in dic1:
                return False
            if word2[i] not in dic2:
                dic2[word2[i]]=1
            else:
                dic2[word2[i]]+=1
        
            
        arr1=list(dic1.values())
        arr2=list(dic2.values())
        for i in arr1:
            if i in arr2:
                arr2.remove(i)
            else:
                return False
        return True
        
        