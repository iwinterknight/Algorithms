'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def brute_force(nums, k):
            res = []
            for i in range(len(nums)-k+1):
                window = nums[i:i+k]
                res.append(max(window))
            return res


        def efficient(nums, k):
            res = []
            q = []
            l = r = 0
            while r < len(nums):
                while q and nums[q[-1]] < nums[r]:
                    q.pop()
                q.append(r)

                if l > q[0]:
                    q.pop(0)

                if r + 1 >= k:
                    res.append(nums[q[0]])
                    l += 1
                r += 1
            return res


        # return brute_force(nums, k)
        return efficient(nums, k)