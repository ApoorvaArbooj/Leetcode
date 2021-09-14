# -*- coding: utf-8 -*-
"""Leetcode 142 Linked List Cycle II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z70vtYsS1I_oaE_gbEFJendIX6TXMQVI
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return None
        slow_pointer = head
        fast_pointer = head
        while(fast_pointer is not None and fast_pointer.next is not None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if(fast_pointer == slow_pointer):
                slow_pointer = head
                while(slow_pointer != fast_pointer):
                    slow_pointer = slow_pointer.next
                    fast_pointer = fast_pointer.next
                return fast_pointer
        return None

