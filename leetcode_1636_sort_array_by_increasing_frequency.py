# -*- coding: utf-8 -*-
"""Leetcode 1636 Sort Array by Increasing Frequency.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FwHIi_I_YjWhhPGBjh4P_xn-aFawkPRe
"""

class Solution:
    def frequencySort(self, nums):
        mapping = {}
        for n in nums:
            if n in mapping:
                mapping[n] += 1
            else:
                mapping[n] = 1
        mapping = {k:v for k,v in sorted(mapping.items(), key=lambda mapping: (mapping[1],-mapping[0]))}
        result = []
        for k,v in mapping.items():
            result.extend([k]*v)
        return result

s=Solution()

print(f'Output: {s.frequencySort(nums = [1,1,2,2,2,3])}')

print(f'Output: {s.frequencySort(nums = [2,3,1,3,2])}')
