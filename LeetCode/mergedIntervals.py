# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:01:15 2017

@author: zhang_000
"""

#merge interval
import operator
def mergeInterval(intervals):
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    intervals.sort(key = operator.itemgetter(0))
    mergedIntervals = []
    start = intervals[0][0]
    end = intervals[0][1]        
    for i in range(len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            mergedIntervals.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    mergedIntervals.append([start, end])
    return mergedIntervals

import bisect
def mergeIntervalPeakMemory(intervals):
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    intervals.sort(key = operator.itemgetter(0))
    mergedIntervals = []
    maxMemory = [0,0,0]
    while len(intervals) > 1:
        t1 = intervals.pop(0)
        t2 = intervals.pop(0)
        newInt = mergeTwoIntervals(t1, t2)
        if newInt[0][2] > maxMemory[2]:
            maxMemory = [item for item in newInt[0]]
        intervals = [newInt[1]] + intervals
        if len(newInt) == 3:
            start = newInt[2][0]
            idx = bisect.bisect_left([inter[0] for inter in intervals], start)
            intervals.insert(idx, newInt[2])
        print intervals
        print maxMemory
    inter = intervals.pop()
    if inter[2] > maxMemory[2]:
            maxMemory = [item in inter]    
    return maxMemory
    
def mergeTwoIntervals(t1, t2):
    if t1[1] <= t2[0]:
        return [t1, t2]
    if t1[1] >= t2[1]:
        newInt = []
        newInt.append([t1[0], t2[0], t1[2]])
        newInt.append([t2[0], t2[1], t1[2] + t2[2]])
        newInt.append([t2[1], t1[1], t1[2]])
    else:
        newInt = []
        newInt.append([t1[0], t2[0], t1[2]])
        newInt.append([t2[0], t1[1], t1[2] + t2[2]])
        newInt.append([t1[1], t2[1], t2[2]])
    return newInt

    
