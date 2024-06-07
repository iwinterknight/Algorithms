'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recursive(prices, b=None, s=None, i=0, profit=0):
            if i >= len(prices):
                if b is not None:
                    return profit + (prices[-1] - prices[b])
                return profit

            if b is None:
                return max(recursive(prices, i, None, i+1, profit-prices[i]), recursive(prices, None, None, i+1, profit))
            if b is not None and s is None:
                return max(recursive(prices, None, None, i+2, profit+prices[i]), recursive(prices, b, None, i+1, profit))


        def memoization(prices, b=None, s=None, i=0, profit=0, cache={}):
            if i >= len(prices):
                if b is not None:
                    return profit + (prices[-1] - prices[b])
                return profit

            if (i, s) in cache:
                return cache[(i, s)]

            if b is None:
                max_profit = max(memoization(prices, i, None, i+1, profit-prices[i], cache), memoization(prices, None, None, i+1, profit, cache))
                cache[(i, s)] = max_profit
                return max_profit
                
            if b is not None and s is None:
                max_profit = max(memoization(prices, None, None, i+2, profit+prices[i], cache), memoization(prices, b, None, i+1, profit, cache))
                cache[(i, s)] = max_profit
                return max_profit

        
        return recursive(prices)
        # return memoization(prices)