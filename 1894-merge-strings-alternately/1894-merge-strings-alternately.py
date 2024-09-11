class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=''
        for i in range(0,min(len(word1),len(word2))):
            output=output+str(word1[i])+str(word2[i])
        if len(word1)!=len(word2):
            if len(word1)>len(word2):
                output=output+word1[min(len(word1),len(word2)):]
            else:
                output=output+word2[min(len(word1),len(word2)):]

        return output            