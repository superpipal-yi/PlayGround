# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:04:16 2017

@author: zhang_000
"""

#binary tree upside down
def upsideDownBinaryTree(root):
    [root, node] = helper(root)
    return root
    

def helper(node):
    if not node:
        return [None, None]
    else:
        if node.left:
            [root, tail] = helper(node.left)
        tail.left = node.right
        tail.right = node
        return [root, node]

def upsideDownBinaryTreeIter(root):
    if not root:
        return None
    
    parent = root.left
    node = root
    rightLeaf = node.right
    while parent:
        curParent = parent
        parent = curParent.left
        newRightLeaf = curParent.right
        curParent.left = rightLeaf
        rightLeaf = newRightLeaf
        curParent.right = node
        node = curParent
        
   return node     
        
