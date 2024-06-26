'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_pointer_approach(nums):
            nums.sort()
            res = []
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]:
                    continue
                l, r = i + 1, len(nums)-1
                sum = 0
                while l < r:
                    sum = num + nums[l] + nums[r]
                    if sum < 0:
                        l += 1
                    elif sum > 0:
                        r -= 1
                    else:
                        res.append([num, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            return res


        def hashing_approach(nums):
            dups = set()
            res = []
            nums.sort()
            for i, num in enumerate(nums):
                if num not in dups:
                    dups.add(num)
                    seen = {}
                    for j in range(i+1, len(nums)):
                        complement = -(num + nums[j])
                        if complement in seen and seen[complement] == i:
                            triplet = [num, nums[j], complement]
                            if triplet not in res:
                                res.append(triplet)
                        seen[nums[j]] = i
            return res


        return two_pointer_approach(nums)
        # return hashing_approach(nums)