class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # new=[]
       
        # for i in range (0,len(nums)):
        #     product=1
        #     for j in range (0,len(nums)):
        #         if i!=j:
        #             if(nums[j]==0):
        #                 product=0
        #                 break
        #             product=product*nums[j]
        #     new.append(product)
        # return new 
        num=nums.copy()
        # count=nums.count(0)
        # for i in range(0,count):
        #     if 0 in num:
        #         num.remove(0)
        # print(nums)

        product=prod(nums)
        for i in range(0,len(nums)):
            if (nums[i])==0:
                num[i]=1
                nums[i]=prod(num)
                num[i]=0
            else:
                nums[i]=product//nums[i]
        return(nums)
