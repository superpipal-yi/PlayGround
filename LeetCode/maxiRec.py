# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 22:55:26 2017

@author: zhang_000
"""

def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
        maxLength = 1 if '1' in matrix else 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    maxLength = max(maxLength, dp[i][j])
        return maxLength**2            