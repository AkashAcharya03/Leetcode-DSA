class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):

            leftsum=sum(nums[0:i])
            rigthsum=sum(nums[i+1:])
            if leftsum==rigthsum:
                return i
        return -1

        # li=0
        # ri=len(nums)-1
        # leftsum=0
        # rightsum=0
        # for i in range(0,len(nums)):
        #     if li!=ri:
        #         if leftsum<=rightsum:
        #             leftsum=leftsum+nums[li]
        #             print(leftsum)

        #             li+=1
        #         elif leftsum>rightsum:
        #             rightsum=rightsum+nums[ri]
        #             print(rightsum)

        #             ri-=1
        #     else:
        #         if leftsum==rightsum:
        #             return li
        # return -1
