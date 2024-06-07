'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(matrix, target):
            top, bottom = 0, len(matrix)-1
            while top <= bottom:
                mid = (top + bottom) // 2
                if target > matrix[mid][-1]:
                    top = mid + 1
                elif target < matrix[mid][0]:
                    bottom = mid - 1
                else:
                    break

            if top <= bottom:
                row = (top + bottom) // 2
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][mid] == target:
                        return True
                    if target > matrix[row][mid]:
                        l = mid + 1
                    elif target < matrix[row][mid]:
                        r = mid - 1 
            return False

        return search(matrix, target)