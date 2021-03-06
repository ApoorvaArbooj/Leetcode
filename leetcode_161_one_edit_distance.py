# -*- coding: utf-8 -*-
"""Leetcode 161 One Edit Distance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C4Qd4FXqegTYSU1dAsm9eND7YOw31yY-
"""

class Solution:
    def isOneEditDistance(self, s,t):
        ns,nt=len(s),len(t)
        if ns>nt:
            return self.isOneEditDistance(t,s)
        if nt-ns>1:
            return False
        if not t and not s:
            return False
        if not t or not s:
            return True
        
        for i in range(ns):
            if s[i] != t[i]:
                if ns==nt:
                    return s[i+1:]==t[i+1:]
                else:
                    return s[i:]==t[i+1:]
            
        # only last character in t differs
        # s = ab t=abz
        return ns+1 == nt

s = Solution()

print(f'Output: {s.isOneEditDistance(s = "ab", t = "acb")}')

print(f'Output: {s.isOneEditDistance(s = "", t = "")}')

print(f'Output: {s.isOneEditDistance(s = "", t = "A")}')

print(f'Output: {s.isOneEditDistance(s = "a", t = "A")}')

