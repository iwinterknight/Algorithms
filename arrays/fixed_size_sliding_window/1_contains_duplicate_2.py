'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def hashing_approach(nums, k):
            seen = dict()
            for i in range(len(nums)):
                if nums[i] in seen and i - seen[nums[i]] <= k:
                    return True
                seen[nums[i]] = i
            return False

        def sliding_window_approach(nums, k):
            l, r = 0, 0
            window = set()
            while r < len(nums):
                if r - l > k:
                    window.remove(nums[l])
                    l += 1
                if nums[r] in window:
                    return True
                window.add(nums[r])
                r += 1
            return False

        # return hashing_approach(nums, k)
        return sliding_window_approach(nums, k)
