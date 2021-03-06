# -*- coding: utf-8 -*-
"""Leetcode 74 Search a 2D Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PmGAHJ-u1ZIhdj1cS-oB6c63Jz5NtBxt
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        if nrows == 0:
            return False
        ncols = len(matrix[0])
        pL = 0
        pR = nrows*ncols - 1
        while pL<=pR:
            mid_indx = (pL+pR)//2
            mid_element = matrix[mid_indx//ncols][mid_indx%ncols]
            if target == mid_element:
                return True
            if target < mid_element:
                pR = mid_indx - 1
            else:
                pL = mid_indx + 1
        return False

s = Solution()

print(f'Output: {s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)}')

