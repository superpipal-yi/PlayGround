# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:29:50 2017

@author: zhang_000
"""

#factor combination
import numpy as np
def getFactors(n):
    if n <= 1:
        return [n]
    else:
        return factor(n, 2, [], [])
        
def factor(n, i, combi, combis):
    while i * i <= n:
        if n % i == 0:
            combis += combi + [i, n/i],
            factor(n/i, i, combi+[i], combis)
        i += 1
    return combis
    