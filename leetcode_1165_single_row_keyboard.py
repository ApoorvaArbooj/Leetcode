# -*- coding: utf-8 -*-
"""Leetcode 1165 Single-Row Keyboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NH4c5HTqyaAhRXZA0uTJe7OcwwrLCBUV
"""

def calculateTime(keyboard, word):
  location_dict = dict(zip(list(keyboard), range(len(keyboard))))
  instr = keyboard[0] + word #Adding 'a' in the start because the finger starts from 0 or 'a'
  distances = [abs(location_dict[instr[i]] - location_dict[instr[i+1]]) for i in range(len(instr)-1)]
  return(sum(distances))

#Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
#Output: 4
#Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
#Total time = 2 + 1 + 1 = 4.

keyboard = "abcdefghijklmnopqrstuvwxyz"
word1 = "cba"
word2 = "leetcode"

print(f'Output: {calculateTime(keyboard,word1)}')

print(f'Output: {calculateTime(keyboard,word2)}')

