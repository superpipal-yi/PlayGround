# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:16:17 2017

@author: zhang_000
"""

#Meeting Rooms II 
def minMeetingRooms(intervals):
    from Queue import PriorityQueue
    if not intervals:
        return 0
    else:
        q = PriorityQueue()
        for i in range(len(intervals)):
            q.put([intervals[i][0], i, 'start'])
        maxRoom = 0
        currentRoom = 0
        while q.qsize() > 0:
            
            time, idx, status = q.get()
            if status == 'start':
                currentRoom += 1
                maxRoom = max(maxRoom, currentRoom)
                q.put([intervals[idx][1], idx, 'end'])
            else:
                currentRoom -= 1
        return maxRoom        
    