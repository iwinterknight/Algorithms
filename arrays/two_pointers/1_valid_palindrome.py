'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def method_1(s):
            s = s.lower()
            s_ = ""
            for c in s:
                if ord(c) in range(97, 122) or ord(c) in range(48, 58):
                    s_ += c
            s = s_
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        def method_2(s):
            s = s.lower()
            s_ = ""
            for c in s:
                if ord(c) in range(97, 122) or ord(c) in range(48, 58):
                    s_ += c
            s = s_
            
            n = len(s)
            if n % 2 != 0:
                mid = n // 2
                i, j = mid, mid
                while i >= 0 and j < n:
                    if s[i] != s[j]:
                        return False
                    i -= 1
                    j += 1
                return True
            else:
                i, j = n // 2 - 1, n // 2
                while i >= 0 and j < n:
                    if s[i] != s[j]:
                        return False
                    i -= 1
                    j += 1
                return True

        return method_1(s)
        # return method_2(s)