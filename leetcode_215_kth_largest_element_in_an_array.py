# -*- coding: utf-8 -*-
"""Leetcode 215 Kth Largest Element in an Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P97FDZbjXS5-5zmwVZWOs9ANRTMpvjaR
"""

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap,n)
            else:
                heapq.heappushpop(heap,n)
        return heapq.heappop(heap)

s = Solution()

print(f'Output: {s.findKthLargest(nums = [3,2,1,5,6,4], k = 2)}')

print(f'Output: {s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)}')

