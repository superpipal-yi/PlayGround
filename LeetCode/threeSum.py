# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:39:21 2017

@author: zhang_000
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        exists = set()
        results = []
        current = None
        for i in range(len(nums)-1):
            if nums[i] == current:
                continue
            else:
                current = nums[i]
                secondPart = self.twoSum(nums[i+1:], 0 - nums[i])
                if secondPart:
                    for s in secondPart:
                        combi = [nums[i]] + s
                        if str(sorted(combi)) not in exists:
                            results.append(combi)
                            exists.add(str(sorted(combi)))
        return results                
        
    
    def twoSum(self, nums, target):
        if not nums:
            return None
        else:
            p1 = 0
            p2 = len(nums)-1
            results = []
            while p2 > p1:
                if nums[p1] + nums[p2] == target:
                    results.append([nums[p1], nums[p2]])
                    p1 += 1
                else:
                    if nums[p1] + nums[p2] < target:
                        p1 +=1
                    else:
                        p2 -= 1
            return results            
                        
            