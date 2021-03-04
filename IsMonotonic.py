#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 07:46:48 2020

@author: nitinkotcherlakota
"""

def isMonotonic(array):
    # Write your code here.
    i,j = 0,1
    if len(array) <= 2:
        return True
    else:
        while array[i] == array[j] and j < len(array)-1:
            i += 1
            j += 1           
        if array[i] < array[j]:
            while j < len(array)-1:
                i += 1
                j += 1
                if array[i] > array[j]:
                    return False
            return True
        elif array[i] > array[j]:
            while j < len(array) - 1:
                i += 1
                j += 1
                if array[i] < array[j]:
                    return False
            return True
        return True
print(isMonotonic([-1, -1, -1, -1, -1, -1, -1, -1]))
