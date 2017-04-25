# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:20:14 2017

@author: zhang_000
"""
#combination sum III

def combinationSum3(k, n):
    res = []
    helper(range(1,10), n, k, [],res)
    return res
    
def helper(nums, target, k, cur, res):
    if not nums or nums[0]> target and target != 0:
        return
    if len(cur) == k:
        res.append(list(cur))
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                break
            cur.append(nums[i])
            helper(nums[i+1:], target - nums[i], k, cur, res)
            cur.pop()
            