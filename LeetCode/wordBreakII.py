# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:25:40 2017

@author: zhang_000
"""

#word break II
def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        D = {}
        D[0] = []
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                D[i] = [s[:i]]
            else:
                D[i] = []
            for j in range(1, i):
                print j
                if not D[j]:
                    continue
                print j
                D[i] += [head + ' ' + s[j:i] for head in D[j] if s[j:i] in wordDict]
        return [d.lstrip() for d in D[len(s)]]   