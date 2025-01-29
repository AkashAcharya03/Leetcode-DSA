class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        k=[]
        nums.clear()
        for n in hashmap:
            nums.append(int(n))
        print(nums)