# -*- coding: utf-8 -*-
"""Leetcode 234 Palindrome Linked List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ov9qDU2Ra0zIQYw3tbYHf_huBI0xEWKk
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head.next:
            return True
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        i,j = 0,len(stack)-1
        while i<=j:
            if stack[i] != stack[j]:
                return False
            i,j = i+1,j-1
        return True