# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:12:12 2017

@author: zhang_000
"""

#Minimum Window Substring
from collections import Counter
def minWindow(s, t):
    if not s:
        return ''
    else:
        loc = {}
        t = Counter(t)
        currentStr = []
        minimumStr = None
        for c in s:
            
            if c in t:
                currentStr.append(c)
                if c in loc:
                    loc[c] += 1
                else:
                    loc[c] = 1
                if len(loc) == len(t):
                    if all(loc[c] >= t[c] for c in loc):
                        currentStr = refine(currentStr, loc, t)
                        if not minimumStr:
                            minimumStr = [c for c in currentStr]
                        else:
                            if len(minimumStr) > len(currentStr):
                                minimumStr = [c for c in currentStr]
            elif currentStr:
                currentStr.append(c)
            print minimumStr    
        if not minimumStr:
             return ''
        else:
             return ''.join(minimumStr)

def refine(currentStr, loc, t):
    if loc[currentStr[0]] <= t[currentStr[0]]:
        return currentStr
    else:
        c = currentStr.pop(0)
        loc[c] -= 1
        while currentStr[0] not in loc or loc[currentStr[0]] > t[currentStr[0]]:
            c = currentStr.pop(0)
            if c in loc:
                loc[c] -= 1
        return currentStr                    
                
                
            
            
        