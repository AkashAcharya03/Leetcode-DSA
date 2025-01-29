class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        prev = nums[0]

        if len(nums) == 1:
            if prev >= target:
                return 0
            else:
                return 1

        for i in range(1, len(nums)):
            if target <=prev:
                return i - 1
            elif nums[i] == target:
                return i
            elif prev <= target and nums[i] >= target:
                return i
            prev = nums[i]
        return len(nums)
