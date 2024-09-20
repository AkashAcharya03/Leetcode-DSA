class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # maxcount=0
        # if nums.count(1)==len(nums):
        #     return len(nums)-1
        # for i in range(0,len(nums)):
        #     count=0
        #     flag=0
        #     if nums[i]==1:
        #         for k in range(i,len(nums)):
        #             if nums[k]==0 and flag==0:
        #                 flag=1
        #             elif nums[k]==0 and flag==1:
        #                 break
        #             elif nums[k]==1:
        #                 count+=1
        #                 maxcount=max(maxcount,count)
        # return maxcount


        left = 0
        maxcount = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            maxcount = max(maxcount, right - left)

        return maxcount

            