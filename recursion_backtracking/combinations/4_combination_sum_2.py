'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack_1(candidates, target, i, curr, curr_sum, res):
            if curr_sum == target:
                if curr not in res:
                    res.append(curr[:])
                return

            if i >= len(candidates) or curr_sum > target:
                return

            curr_sum += candidates[i]
            curr.append(candidates[i])
            backtrack_1(candidates, target, i+1, curr, curr_sum, res)
            curr_sum -= candidates[i]
            curr.pop()
            backtrack_1(candidates, target, i+1, curr, curr_sum, res)


        def backtrack_2(candidates, target, start, curr, curr_sum, res):
            if curr_sum == target:
                if curr not in res:
                    res.append(curr[:])
                return

            if start >= len(candidates) or curr_sum > target:
                return

            prev = None
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num != prev:
                    curr.append(num)
                    curr_sum += num
                    backtrack_2(candidates, target, i+1, curr, curr_sum, res)
                    curr.pop()
                    curr_sum -= num
                    prev = num               


        # res = []
        # backtrack_1(sorted(candidates), target, 0, [], 0, res)
        # return res

        res = []
        backtrack_2(sorted(candidates), target, 0, [], 0, res)
        return res