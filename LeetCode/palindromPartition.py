# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:03:43 2017

@author: zhang_000
"""

def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if not s:
        return []
    else:
        res = []
        helper(s, res, [])
        return res
        
def ifPalindrome(s):
    if not s:
        return True
    else:
        i  = 0
        j = len(s) - 1
        while j >= i:
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1
        return True
        
def helper(s, res, cur):
    if not s:
        res.append(cur)
    for i in range(1, len(s) + 1):
        if ifPalindrome(s[:i]):
            cur += [s[:i]]
            helper (s[1+i:], res, cur)
            cur.pop()