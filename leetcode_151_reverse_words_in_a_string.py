# -*- coding: utf-8 -*-
"""Leetcode 151 Reverse Words in a String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFFcTs6p0YnCx5hgdRmJsJDIso36-GP3
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
        #Algorithm
        #Convert to list because strings are immutable in python
        #Reverse the whole string
        #Then reverse each word again

#Input: s = "  hello world  "
#Output: "world hello"
#Explanation: Your reversed string should not contain leading or trailing spaces.

#Input: s = "a good   example"
#Output: "example good a"
#Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

#Input: s = "  Bob    Loves  Alice   "
#Output: "Alice Loves Bob"

s = Solution()

print(f'Output: {s.reverseWords("  hello world  ")}')

print(f'Output: {s.reverseWords("a good   example")}')

