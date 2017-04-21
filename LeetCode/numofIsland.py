# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:16:24 2017

@author: zhang_000
"""
#number of island
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    else:
        m = len(grid)
        n = len(grid[0])
        bitmap = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bitmap.add((i,j))
        numIsland = 0
        while bitmap:            
            start = bitmap.pop()
            numIsland += 1
            
            if not bitmap:
                return numIsland
            update(bitmap, m, n,start)
        return numIsland
        
def update(bitmap, m, n, start):
    parents = [start]
    while parents and bitmap:
        child = []
        for p in parents:
            if p[0]-1 >=0:
                p_up = (p[0] - 1, p[1])
                if p_up in bitmap:
                    bitmap.remove(p_up)
                    child.append(p_up)
            if p[0]+1 <m:
                p_down = (p[0] + 1, p[1])
                if p_down in bitmap:
                    bitmap.remove(p_down)
                    child.append(p_down)
            if p[1]-1 >=0:
                p_left = (p[0], p[1] - 1)
                if p_left in bitmap:
                    bitmap.remove(p_left)
                    child.append(p_left)
            if p[1] + 1 < n:
                p_right = (p[0], p[1] + 1)
                if p_right in bitmap:
                    bitmap.remove(p_right)
                    child.append(p_right)
        parents = list(child)