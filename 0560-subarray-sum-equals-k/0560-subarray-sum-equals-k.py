class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}  # To handle subarrays starting at index 0

        for num in nums:
            prefix_sum += num

            # Check if (prefix_sum - k) exists in hashmap
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]

            # Update hashmap with the current prefix_sum
            if prefix_sum in hashmap:
                hashmap[prefix_sum] += 1
            else:
                hashmap[prefix_sum] = 1

        return count