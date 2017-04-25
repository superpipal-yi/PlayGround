# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:47:03 2017

@author: zhang_000
"""

# subset I
def subsets(self, nums):
    if not nums:
        return []
    res = []
    helper([],res,nums)
    return res + [[]]
def helper(cur, res, nums):
    if not nums:
        return
    else:
        for i in range(len(nums)):
            cur.append(nums[i])
            res.append(list(cur))
            helper(cur, res, nums[1+i :])
            cur.pop()
    
