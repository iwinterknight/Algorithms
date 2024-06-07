'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def edgeMaxSum(nums):
            min_so_far, min_sum = 0, float('inf')
            total = 0
            for i in range(len(nums)):
                min_so_far += nums[i]
                total += nums[i]
                min_sum = min(min_so_far, min_sum)
                min_so_far = min(min_so_far, 0)
            return total - min_sum

        def centerMaxSum(nums):
            max_so_far, max_sum = 0, float('-inf')
            for i in range(len(nums)):
                max_so_far += nums[i]
                max_sum = max(max_sum, max_so_far)
                max_so_far = max(max_so_far, 0)
            return max_sum

        
        edge_sum = edgeMaxSum(nums)
        center_sum = centerMaxSum(nums)
        if edge_sum == 0:
            return center_sum
        return max(center_sum, edge_sum)