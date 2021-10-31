# -*- coding: utf-8 -*-
"""Leetcode 242 Valid Anagram.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fiomIsG0fi8JJYFqcpHuR981QU_v5JM8
"""

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        U 
        s = "anagram"
        t = "nagaram"
        O/P: true
        
        s = "a"
        t = "va"
        O/P: false
        
        s = "a"
        t = "a"
        O/P: true
        
        M
        string manipulation
        
        P
        find the count of each letter and compare it with the other string
        I
        R
        E time: O(n) space: O(m) m is unique characters
        space: O(1) if we build a hashtable of the 26 alphabets because the size will remain same (only 26 alphabets).
        """
        if len(s) != len(t):
            return False
        letter_counter = Counter(s)
        for ch in t:
            if ch not in letter_counter:
                return False
            else:
                if letter_counter[ch] <= 0:
                    return False
                else:
                    letter_counter[ch] -= 1
        return True

s = Solution()

print(f'Output: {s.isAnagram(s="anagram",t="nagaram")}')

print(f'Output: {s.isAnagram(s="va",t="a")}')
