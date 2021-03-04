#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:55:53 2020

@author: nitinkotcherlakota
"""

#Amazon music pairs

def pairs(l):
    count = 0
    temp = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if (l[i] + l[j]) % 60 == 0 and sorted((i,j)) not in temp:
                temp.append((i,j))
                count += 1
    return count
    

print(pairs([60, 60, 60]))
print(pairs([10, 50, 90, 30]))
print(pairs([30, 20, 150, 100, 40]))
print(pairs([18,42,60]))