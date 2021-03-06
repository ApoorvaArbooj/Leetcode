# -*- coding: utf-8 -*-
"""Leetcode 35 Search Insert Position.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n3YPFMDwpiHwR1oTQvVy5T8qjLKyjDn2
"""

class Solution:
    def searchInsert(self, nums, target):
        i=0
        j=len(nums)-1
        
        while i<=j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return i

s = Solution()

print(f'Output: {s.searchInsert(nums = [1,3,5,6], target = 5)}')

print(f'Output: {s.searchInsert(nums = [1,3,5,6], target = 7)}')

