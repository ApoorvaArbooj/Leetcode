# -*- coding: utf-8 -*-
"""Leetcode 1720 Decode XORed Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZsVMPS8kyArGoyZrg-ydKb6r1ta_5hO3
"""

def decode(encoded, first):
  result = [first]
  for e in encoded:
    result.append(result[-1]^e)
  return result

#Input: encoded = [1,2,3], first = 1
#Output: [1,0,2,1]
#Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

ip_encoded = [1,2,3]
ip_first = 1

print(f'Output:{decode(ip_encoded,ip_first)}')
