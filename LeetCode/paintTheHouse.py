# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:16:54 2017

@author: zhang_000
"""

#paint house
def paintHouseI(cost, n):
    # dp[i][j] = the minimum cost until paint house i with color j
    if n == 0:
        return 0
    dp = [[0] * n for i in range(3)]
    for i in range(3):
          dp[0][i] = cost[0][i]
    for i in range(1, n):
        for j in range(3):
            idx = [1,2,3]
            idx.remove(j)
            dp[i][j] = cost[i][j] + min(dp[i-1][idx[0]], dp[i-1][idx[1]])
    return min(dp[-1][0], dp[-1][1], dp[-1][2])        