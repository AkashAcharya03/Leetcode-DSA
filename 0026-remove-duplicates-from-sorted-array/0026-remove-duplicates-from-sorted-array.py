class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        nums.clear()
        for n in hashmap:
            nums.append(int(n))
        print(nums)
        # prev=nums[0]
        # new=[]
        # new.append(nums[0])
        # for i in range(1,len(nums)):
        #     if prev!=nums[i]:
        #         prev=nums[i]
        #         new.append(int(prev))
        # nums.clear()
        # nums=new
        # return(nums)
