'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def brute_force(nums, k):
            count = 0
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    if sum(nums[i:j+1]) == k:
                        count += 1
            return count
        
        
        def prefix_sums_approach(nums, k):
            prefix_sums = []
            cumulative = 0
            for num in nums:
                cumulative += num
                prefix_sums.append(cumulative)
            num_sums = 0
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    lsum, rsum = 0, prefix_sums[j]
                    if i-1 >= 0:
                        lsum = prefix_sums[i-1]
                    if rsum - lsum == k:
                        num_sums += 1
            return num_sums


        def hashing_approach(nums, k):
            hashmap = {0: 1}
            cumulative = 0
            count = 0
            for i, num in enumerate(nums):
                cumulative += num
                if cumulative - k in hashmap:
                    count += hashmap[cumulative - k]
                if cumulative in hashmap:
                    hashmap[cumulative] += 1
                else:
                    hashmap[cumulative] = 1
            return count


        # return brute_force(nums, k)
        return prefix_sums_approach(nums, k)
        # return hashing_approach(nums, k)