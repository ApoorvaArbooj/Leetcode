# -*- coding: utf-8 -*-
"""Leetcode 445 Add Two Numbers II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wyqJKvMxTsaqhp2sFk6Fz4_G27yfxrI_
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        reverse_l1 = self.reverse_linklist(l1)
        reverse_l2 = self.reverse_linklist(l2)

        reverse_addition_result = self.addTwoReversedNumbers(reverse_l1,reverse_l2)

        return self.reverse_linklist(reverse_addition_result)

    def reverse_linklist(self, l1):
       prevNode = None
       currNode = l1
       nextNode = None
       while currNode is not None:
           nextNode = currNode.next
           currNode.next = prevNode
           prevNode = currNode
           currNode = nextNode
       return prevNode
    
    def addTwoReversedNumbers(self, l1, l2):
        currNode1 = l1
        currNode2 = l2
        result_carry= 0
        dummy_Head = ListNode(0)
        currNode = dummy_Head
        while currNode1 or currNode2:
            if not currNode1:
                value1 = 0
            else:
                value1 = currNode1.val
            if not currNode2:
                value2 = 0
            else:
                value2 = currNode2.val
            
            result_carry,result_sum = divmod(value1+value2+result_carry,10)
            
            currNode.next = ListNode(result_sum)
            currNode = currNode.next
            
            if currNode1:
                currNode1 = currNode1.next
            if currNode2:
                currNode2 = currNode2.next
        
        if result_carry >= 1:
            currNode.next = ListNode(result_carry)
        return dummy_Head.next

node4_l1 = ListNode(3)
node3_l1 = ListNode(4)
node3_l1.next = node4_l1
node2_l1 = ListNode(2)
node2_l1.next = node3_l1
head_l1 = ListNode(7)
head_l1.next = node2_l1

ll1 = head_l1
while ll1:
    print(f'{ll1.val}')
    ll1 = ll1.next

node3_l2 = ListNode(4)
node2_l2 = ListNode(6)
node2_l2.next = node3_l2
head_l2 = ListNode(5)
head_l2.next = node2_l2

ll2 = head_l2
while ll2:
    print(f'{ll2.val}')
    ll2 = ll2.next

s = Solution()

addition_result = s.addTwoNumbers(head_l1,head_l2)

res = addition_result
while res:
    print(f'{res.val}')
    res = res.next
