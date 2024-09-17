class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # count1=flowerbed.count(1)
        # if len(flowerbed)%2==0: 
        #     if len(flowerbed)/2 -count1 <=n:
        #         return True
        # else: 
        #     if flowerbed[0]==1 and flowerbed[len(flowerbed)-1]==1:
        #         if (len(flowerbed)+1)/2 -count1 >=n:
        #             return True
        #     elif flowerbed[0]==0 and flowerbed[len(flowerbed)-1]==0:
        #         if (len(flowerbed)-1)/2 -count1 >=n:
        #             return True
        count=0
        if len(flowerbed)==1 :
            if flowerbed[0]==0 and n<=1:
                return True

        for i in range (0,len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    count+=1
            elif i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    count+=1
            else:
                if flowerbed[i+1]==0 and flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    count+=1
        if count>=n:
            return True
        else:
            return False






