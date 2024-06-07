'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        t_counter = Counter(t)

        def check(window):
            for k, v in t_counter.items():
                if k not in window or window[k] < v:
                    return False
            return True

        window = {}
        l, r = 0, 0
        min_len = len(s)+1
        min_win = (l, r)
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            while l <= r and s[r] in window and check(window):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_win = (l, r+1)
                window[s[l]] = window.get(s[l], 0) - 1
                l += 1
            r += 1
        return s[min_win[0]:min_win[1]]