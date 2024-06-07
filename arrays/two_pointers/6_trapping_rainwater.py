'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        def dp(height):
            L, R = [], []
            maxL, maxR = float('-inf'), float('-inf')
            for i in range(len(height)):
                maxL = max(maxL, height[i])
                L.append(maxL)
            for i in range(len(height)-1, -1, -1):
                maxR = max(maxR, height[i])
                R.append(maxR)
            water = 0
            for i in range(len(height)):
                j = len(height)-i-1
                water += (min(L[i], R[j]) - height[i])
            return water


        def two_pointer(height):
            l, r = 0, len(height)-1
            maxL, maxR = 0, 0
            water = 0
            while l < r:
                if height[l] <= height[r]:
                    if height[l] > maxL:
                        maxL = height[l]
                    water += maxL - height[l]
                    l += 1
                else:
                    if height[r] > maxR:
                        maxR = height[r]
                    water += maxR - height[r]
                    r -= 1
            return water

        # return dp(height)
        return two_pointer(height)