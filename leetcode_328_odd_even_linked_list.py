# -*- coding: utf-8 -*-
"""Leetcode 328 Odd Even Linked List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kxuYI935qgj-JA00eWNzRC-R5lHW34qR
"""

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def oddEvenList(self, head):

    count = 0
    dummy_head = ListNode(0)
    dummy_head.next = head
    
    while head:
      evenNode = head
      for i in range(count+1):
        if evenNode.next:
          evenNode = evenNode.next
        else:
          break
      if evenNode.next:
        oddNode = evenNode.next
        evenNode.next = oddNode.next
        oddNode.next = head.next
        head.next = oddNode
        count += 1
        head = head.next
      else:
        break
    
    return dummy_head.next

l6=ListNode(6)
l5 = ListNode(5)
l5.next = l6
l4 = ListNode(4)
l4.next = l5
l3 = ListNode(3)
l3.next = l4
l2 = ListNode(2)
l2.next = l3
head = ListNode(1)
head.next = l2

ll = head
while ll:
  print(ll.val)
  ll = ll.next

s = Solution()

newHead = s.oddEvenList(head)

ll = newHead
while ll:
  print(ll.val)
  ll = ll.next

