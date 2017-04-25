# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:46:11 2017

@author: zhang_000
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        else:
            nums.sort()
            res = []
            used = [False] * len(nums)
            self.helper(nums, used, res, [])
            return res
            
    def helper(self, nums, used, res, cur):
        if all(used):
            res.append(list(cur))
            return
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    self.helper(nums, used, res, cur)
                    cur.pop()
                    used[i] = False
                    
                    