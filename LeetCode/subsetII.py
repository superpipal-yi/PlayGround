# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:24:43 2017

@author: zhang_000
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        else:
            nums.sort()
            res = []
            self.helper(res, [], nums)
            return res + [[]]
            
    def helper(self, res, cur, nums):
        if not nums:
            return
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    cur.append(nums[i])
                    res.append(list(cur))
                    self.helper(res, cur, nums[i+1:])
                    cur.pop()