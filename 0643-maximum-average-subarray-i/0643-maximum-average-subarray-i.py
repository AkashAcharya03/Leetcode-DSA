class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxsum=summ
        for i in range(1,len(nums)-k+1):
            summ = summ - nums[i - 1] + nums[i + k - 1]
            maxsum = max(maxsum, summ)
        return float(maxsum/k)

