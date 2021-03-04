#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:02:46 2020

@author: nitinkotcherlakota
"""

def firstDuplicateValue(array):
    for value in array:
        absv = abs(value)
        print(array[absv - 1], value)
        if array[absv - 1] < 0:
            return absv
        array[absv - 1] *= -1
        print(array)
print(firstDuplicateValue([2,1,5,2,3,3,4]))