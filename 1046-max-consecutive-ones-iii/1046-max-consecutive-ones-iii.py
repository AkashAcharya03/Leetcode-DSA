class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxcount=0
        # for i in range(0,len(nums)):
        #     if maxcount>len(nums)-i:
        #         break
        #     count=0
        #     flag=k
        #     for j in range (i,len(nums)):
        #         if nums[j]==1:
        #             count+=1
        #         elif flag==0 and nums[j]==0:
        #             break
        #         elif nums[j] ==0 and flag>0:
        #             count+=1
        #             flag-=1             

        #         maxcount=max(maxcount,count)
        # return maxcount

        left = 0
        maxcount = 0
        zeros_flipped = 0

        for right in range(len(nums)):
            # Expand the window by adding the current element at 'right'
            if nums[right] == 0:
                zeros_flipped += 1

            # If we have more than 'k' zeros in the window, shrink from the left
            while zeros_flipped > k:
                if nums[left] == 0:
                    zeros_flipped -= 1
                left += 1  # Shrink the window by moving the left pointer

            # Calculate the length of the current valid window
            maxcount = max(maxcount, right - left + 1)

        return maxcount
            