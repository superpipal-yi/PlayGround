# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:56:40 2017

@author: zhang_000
"""

def restoreIpAddresses(s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        else:
            res = []
            helper([],res,s)
            return res
        
def helper(cur, res, s):
    print cur
    print s
    if not s:
        if len(cur) == 4:
            res.append('.'.join(list(cur)))
        return
    if len(cur) == 4:
        return
    
    for i in range(1,min(len(s)+1, 4)):
        if int(s[:i]) <=255 and not (s[0] == '0' and i > 1): 
            cur.append(s[:i])
            helper(cur, res, s[i:])
            cur.pop()
                

