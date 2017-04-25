# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:36:18 2017

@author: zhang_000
"""
'''
#Word Ladder II
def findLadders(beginWord, endWord, wordList):
    if not beginWord or not endWord or not wordList:
        return []
    else:
        res = []
        wList = set(wordList)
        cur = [[[beginWord], wList]]
        maxLength = len(wordList)
        helper(cur, endWord, res, maxLength)
        return res
        
def helper(cur, endWord, res, maxLength):
    p = 0
    while (not res and p < maxLength  and cur): 
        child = []
        for c in cur:
            lastW = c[0][-1]
            wList = set(c[1])
            for i in range(len(lastW)):
                for s in 'abcdefghijklmnopqrstuvwxyz':
                    newW = lastW[:i] + s + lastW[i+1:]
                    if newW != lastW:
                        if newW in wList:
                            newWList = set(wList)
                            newWList.remove(newW)
                            child.append([c[0] + [newW], newWList])
                            if newW  == endWord:
                                res.append(c[0] + [newW])
                            
        cur = list(child)    
        p += 1    
'''        
def findLadders(beginWord, endWord, wordList):
    if not beginWord or not endWord or not wordList:
        return []
    else:
        res = []
        wList = set(wordList)
        nextWord = {k: [] for k in wordList}
        nextWord[beginWord]  = []
        parent = [beginWord]
        while parent and wordList:
            if endWord in parent:
                break
            child = []
            for word in parent:
                for s in 'abcdefghijklm9nopqrstuvwxyz':
                    for i in range(len(word)):
                        newW = word[:i] + s + word[i+1:]
                        if newW != word and newW in wordList:
                            nextWord[word] += [newW]
                            if newW != endWord:
                                wordList.remove(newW)
                            child.append(newW)
            parent = list(child)
         
        constructWordPath(res, nextWord, endWord, [beginWord], beginWord)
        return res
def constructWordPath(res, nextWord, endWord, cur, lastWord):
    if lastWord == endWord:
        return
        
    nextPossibleW = nextWord[lastWord]
    if not nextPossibleW:
        return
    else:
        for w in nextPossibleW:
            cur.append(w)
            if w == endWord:
                res.append(list(cur))
            constructWordPath(res, nextWord, endWord, cur,w)
            cur.pop()
                
            
                        