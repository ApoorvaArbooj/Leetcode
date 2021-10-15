# -*- coding: utf-8 -*-
"""Leetcode 121 Best Time to Buy and Sell Stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b4ZE7JQXektQbR4FjjfEX3ZDIpcqiGbM
"""

class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_buy = float('inf')
        for p in prices:
            if p < min_buy:
                min_buy = p
            else:
                profit = max(profit, p-min_buy)
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = float('inf')
        for p in prices:
            min_buy = min(min_buy,p)
            profit = max(profit,p-min_buy)
        return profit

s = Solution()

print(f'Output: {s.maxProfit(prices = [7,1,5,3,6,4])}')

print(f'Output: {s.maxProfit(prices = [7,6,4,3,1])}')

