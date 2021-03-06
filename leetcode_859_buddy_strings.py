# -*- coding: utf-8 -*-
"""Leetcode 859 Buddy Strings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Op5iULK--6zCCwNyEzWc1raAwDi5l4uz
"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        #if the two strings are not of equal length
        if (len(s) != len(goal)): return False
        
        #if the two strings are equal (same characters)
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False
        
        pairs = [(a,b) for a,b in zip(s,goal) if a != b]
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

#Input: s = "ab", goal = "ba"
#Output: true
#Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

s = Solution()

print(f'Output: {s.buddyStrings(s="ab",goal="ba")}')

