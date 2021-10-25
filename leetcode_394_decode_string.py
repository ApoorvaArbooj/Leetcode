# -*- coding: utf-8 -*-
"""Leetcode 394 Decode String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13-oaD2C2dZ5IWV0De_UIleTkrudVGBPe
"""

from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for i in range(len(s)):
            if s[i] == ']':
                decodedString = ''
                while stack and stack[-1]!='[':
                    decodedString += stack.pop()
                stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    number += stack.pop()
                number = number[::-1]
                for _ in range(int(number)):
                    for dS in decodedString[::-1]:
                        stack.append(dS)
            else:
                stack.append(s[i])
        return ''.join(stack)

s = Solution()

print(f'Output: {s.decodeString(s = "3[a]2[bc]")}')

print(f'Output: {s.decodeString(s ="2[abc]3[cd]ef")}')

