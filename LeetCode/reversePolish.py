# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:46:37 2017

@author: zhang_000
"""

#Reverse Polish Notation
import operator
def evalRPN(tokens):
    if not tokens:
        return 0
    else:
        op = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.div}
        stack = []
        while tokens:
            print stack
            item = tokens.pop(0)
            if item not in op:
                stack.append(float(item))
            else:
                item1 = stack.pop()
                item2 = stack.pop()
                result = reduce(op[item], [item2, item1])
                stack.append(result)
        return stack[0]        
    