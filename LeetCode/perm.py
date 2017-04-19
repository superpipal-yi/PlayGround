# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:37:23 2017

@author: zhang_000
"""

#Permutations
def permute(nums):
    if not nums or len(nums) == 1:
        return nums
    else:
        perm = [[nums[0]]]
        for item in nums[1:]:
            currentPerm = []
            n = len(perm[0])
            for p in perm:
                for i in range(n+1):
                    l = [s for s in p]
                    l.insert(i, item)
                    currentPerm.append(l)
            perm = [p for p in currentPerm]
        return perm        
                