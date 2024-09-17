class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range (0,len(nums)-2):
        #     if nums[i]<nums[i+1]<nums[i+2]:
        #         return True
        # return False
        # for i in range (0,len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]<nums[j]<nums[k]:
        #                 return True
        # return False      
        
        first = float('inf') 
        second = float('inf')  
    
        for num in nums:
            if num <= first:     
                first = num
            elif num <= second:   
                second = num
            else:                
                return True
    
        return False