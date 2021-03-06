# -*- coding: utf-8 -*-
"""Leetcode 230 Kth Smallest Element in a BST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16cWulxkhOVvZ_pQKUwO0iquH6QJoqEmI
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(root):
            if not root:
                return None
            inOrder(root.left)
            if len(self.result) < k:
                self.result.append(root.val)
            else:
                return None
            inOrder(root.right)
        
        
        self.result = []
        inOrder(root)
        return (self.result[-1])