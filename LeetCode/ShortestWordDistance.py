# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:42:38 2017

@author: zhang_000
"""

#shortest word distance

def getShortestWordDistance(S, w1, w2):
    distance = len(S)
    idx1 = -1
    idx2 = -1
    for i in range(len(S)):
        if S[i] == w1:
            idx1 = i
            if idx2 >= 0:
                distance = min(distance, abs(idx1 - idx2))
        elif S[i] == w2:
            idx2 = i
            if idx1 >= 0:
                distance = min(distance, abs(idx1 - idx2))
    return distance

def getShortestWordDistanceFreq(S, w1, w2):
    wordLoc = {}
    for i in range(len(S)):
        if S[i] in wordLoc:
            wordLoc[S[i]] += [i]
        else:
            wordLoc[S[i]] = [i]
    
    idx1 = wordLoc[w1]
    idx2 = wordLoc[w2]
    distance = len(S)
    while idx2 and idx1:
        distance = min(distance, abs(idx2[0] - idx1[0]))
        if idx2[0] < idx1[0]:
            idx2.pop(0)
        else:
            idx1.pop(0)
    return distance

        

            