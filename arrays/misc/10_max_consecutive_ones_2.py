'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s, e = 0, 0
        max_ones = 0
        k = 1
        while e < len(nums):
            if nums[e] == 0:
                k -= 1
            
            while k < 0 and s <= e:
                if nums[s] == 0:
                    k += 1
                s += 1
            
            max_ones = max(max_ones, e-s+1)
            e += 1
        
        return max_ones
