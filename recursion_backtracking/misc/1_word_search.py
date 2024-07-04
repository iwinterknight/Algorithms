'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(board, word, idx, r, c, visited, m, n):
            if idx == len(word):
                return True

            visited.add((r, c))

            steps = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for step in steps:
                i, j = step[0], step[1]
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and board[i][j] == word[idx]:
                    if backtrack(board, word, idx+1, i, j, visited, m, n):
                        return True
            visited.remove((r, c))
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(board, word, 1, i, j, set(), m, n):
                        return True
        return False