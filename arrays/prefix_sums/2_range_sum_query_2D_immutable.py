'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.prefix_sums = [[0 for _ in range(self.n)] for _ in range(self.m)]
        cumulative_sum = 0
        for j in range(self.n):
            cumulative_sum += matrix[0][j]
            self.prefix_sums[0][j] = cumulative_sum
        cumulative_sum = 0
        for i in range(self.m):
            cumulative_sum += matrix[i][0]
            self.prefix_sums[i][0] = cumulative_sum
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.prefix_sums[i][j] = matrix[i][j] + self.prefix_sums[i-1][j] + self.prefix_sums[i][j-1] - self.prefix_sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        col1 -= 1
        row1 -= 1
        lsum, usum = 0, 0
        lusum = 0
        if row1 >= 0:
            usum = self.prefix_sums[row1][col2]
        if col1 >= 0:
            lsum = self.prefix_sums[row2][col1]
        if row1 >= 0 and col1 >= 0:
            lusum = self.prefix_sums[row1][col1]
        return self.prefix_sums[row2][col2] - usum - lsum + lusum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)