class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            leftsum=sum(nums[0:i])
            rigthsum=sum(nums[i+1:])
            if leftsum==rigthsum:
                return i
        return -1