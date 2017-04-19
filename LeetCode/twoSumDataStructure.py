# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:39:05 2017

@author: zhang_000
"""

#two sum data structure
class twoSumData(object):
    
    def __init__(self):
        self.loc = {}
        self.length = 0
        
    def add(self, number): 
        self.length += 1
        if number in self.loc:
            self.loc[number] += [self.length]
        else:
            self.loc[number] = [self.length]

    def find(self, value):
        for k in self.loc:
            num = value - k
            if num  == k:
                if len(self.loc[k]) > 1:
                    return True
            else:
                if num in self.loc:
                    return True
        return False
        