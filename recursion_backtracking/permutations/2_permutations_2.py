'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(counts, curr, res):
            if len(curr) == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return

            for num in counts:
                if counts[num] > 0:
                    curr.append(num)
                    counts[num] -= 1
                    backtrack(counts, curr, res)
                    counts[curr.pop()] += 1

        res = []
        backtrack(Counter(nums), [], res)
        return res

