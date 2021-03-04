#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:58:55 2020

@author: nitinkotcherlakota
"""

#optimal utilization


def optimalUtilization(a, b, target):
    a = sorted(a, key=lambda elem: elem[1], reverse=True)
    b = sorted(b, key=lambda elem: elem[1], reverse=True)

    output = []
    for aElem in a:
        for bElem in b:
            sum = aElem[1] + bElem[1]
            
            if sum == target or (len(output) == 0 and target > sum):
                output.append([aElem[0], bElem[0], sum])
            elif len(output) > 0 and sum < output[-1][2]:
                print(output[-1][2])
                break
            
    return sorted([elem[0:2] for elem in output], key=lambda elem: elem[0])


print(optimalUtilization([[1, 3000], [2, 5000], [3, 7000], [4, 10000]], [[1, 2000], [2,3000], [3, 4000], [4, 5000]], 10000))
#print(optimalUtilization([], [], 7))
#print(optimalUtilization([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7))
#print(optimalUtilization([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10))
#print(optimalUtilization([[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20))
#print(optimalUtilization([[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20))
#print(optimalUtilization([[1, 1]], [[1, 3], [2, 3], [3, 3]], 4))

3,4,5,6,7,8,9,10,11,12,13

            8
        5       11
      4   7    10 12
     3   6    9     13