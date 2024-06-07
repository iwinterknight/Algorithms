'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, res):
            if len(curr) == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr, res)
                    curr.pop()
            
        if not nums:
            return []
        res = []
        backtrack(nums, [], res)
        return res
        