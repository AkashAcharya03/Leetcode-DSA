class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array=[[],[]]
        for i in nums1:
            if i not in nums2:
                if i not in array[0]:
                    array[0].append(i)
        for i in nums2:
            if i not in nums1:
                if i not in array[1]:

                    array[1].append(i)
        return(array)
