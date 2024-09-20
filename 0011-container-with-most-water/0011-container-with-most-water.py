class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxquantity=0
        # for i in range(0,len(height)-1):
        #     for j in range(i+1,len(height)):
        #         maxquantity=max(min(height[i],height[j])*(j-i),maxquantity)
        # return(maxquantity)
            
        left = 0
        right = len(height) - 1
        maxquantity = 0
        
        while left < right:
            maxquantity = max(min(height[left], height[right]) * (right - left), maxquantity)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxquantity      
