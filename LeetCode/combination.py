# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:10:54 2017

@author: zhang_000
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return[]
        else:
            res = []
            nums = range(1, n+1)
            self.helper(nums, [], res, k)
            return res
            
    def helper(self, nums, cur, res, k):
        if len(cur) == k:
            res.append(list(cur))
            return
        if k - len(cur) > len(nums):
            return
        else:
            for i in range(len(nums)):
                cur.append(nums[i])
                self.helper(nums[i+1:], cur, res, k)
                cur.pop()
                    