# -*- coding: utf-8 -*-
"""Leetcode 739 Daily Temperatures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1diM8V9nTX3fNMRve2fUOgwEtYbFwtxHV
"""

def dailyTemperatures(temperatures):
    answer = [0]*len(temperatures)
    stack= []
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]]<temperatures[i]:
            top = stack.pop()
            answer[top] = i-top
        stack.append(i)
    return answer

dailyTemperatures([73,74,75,71,69,72,76,73])

