# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:29:59 2017

@author: zhang_000
"""

#Product of Array Except Self
def productExceptSelf(nums):
    if not nums: 
        return nums
    else:
        f = [1]
        for item in nums[:-1]:
            f.append(f[-1] * item)
        factor = nums[-1]
        for i in range(len(f) - 2, -1, -1):
            f[i] *= factor
            factor *= nums[i]
        return f