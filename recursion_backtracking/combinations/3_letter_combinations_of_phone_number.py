'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def backtrack(digits, idx, curr, res):
            if idx == len(digits):
                res.append(curr)
                return

            for lttr in letters[digits[idx]]:
                curr += lttr
                backtrack(digits, idx+1, curr, res)
                curr = curr[:-1]
               
        if not digits:
            return []
        
        res = []
        backtrack(digits, 0, "", res)
        return res