'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, i, curr, res):
            if i >= len(nums):
                if curr not in res:
                    res.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(nums, i+1, curr, res)
            curr.pop()
            backtrack(nums, i+1, curr, res)

        res = []
        backtrack(sorted(nums), 0, [], res)
        return res