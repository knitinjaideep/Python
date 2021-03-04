#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:06:19 2020

@author: nitinkotcherlakota
"""

#Find all permutations that add upto 12
#Exxpected: [[3,4,5],[5,6,1],[4,6,2],[6,6]]


def permutationsSum(array,target):
    permutations = []
    permutationHelper(1, array, target, permutations)
    return permutations

def permutationHelper(index, array, target,permutations):
    if index < 0:
        return []
    if array[:index]
            
            
print(permutationsSum([3,4,5,6,1,4,2,6],12))

stack = []
