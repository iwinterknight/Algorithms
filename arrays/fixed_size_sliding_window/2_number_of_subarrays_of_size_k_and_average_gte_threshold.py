'''Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
'''


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num_arrays, curr_sum = 0, 0
        l, r = 0, 0
        while r < len(arr):
            if r-l+1 > k:
                curr_sum -= arr[l]
                l += 1
            curr_sum += arr[r]
            if r-l+1 == k and curr_sum // k >= threshold:
                num_arrays += 1
            r += 1
        return num_arrays