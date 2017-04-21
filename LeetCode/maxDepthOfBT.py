# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:50:06 2017

@author: zhang_000
"""

#Maximum Depth of Binary Tree
def maxDepth(root):
    if not root:
        return 0
    parent = [root]
    depth = 0
    while parent:
        depth += 1
        child = []
        for p in parent:
            if p.left:
                child.append(p.left)
            if p.right:
                child.append(p.right)
        parent = [c for c in child]
    return depth        