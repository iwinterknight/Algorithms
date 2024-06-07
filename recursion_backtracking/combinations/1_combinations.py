'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack_1(n, k, start, curr, res):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(start, n+1):
                curr.append(i)
                backtrack_1(n, k, i+1, curr, res)
                curr.pop()


        def backtrack_2(n, k, i, curr, res):
            if len(curr) == k:
                res.append(curr[:])
                return

            if i > n:
                return
            curr.append(i)
            backtrack_2(n, k, i+1, curr, res)
            curr.pop()
            backtrack_2(n, k, i+1, curr, res)


        res = []
        # backtrack_1(n, k, 1, [], res)
        backtrack_2(n, k, 1, [], res)
        return res