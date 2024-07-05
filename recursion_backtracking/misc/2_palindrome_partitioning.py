'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]


Example 2:

Input: s = "a"
Output: [["a"]]
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        def backtrack(s, i, curr, res):
            if i >= len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    curr.append(s[i:j+1])
                    backtrack(s, j+1, curr, res)
                    curr.pop()

        
        res = []
        backtrack(s, 0, [], res)
        return res