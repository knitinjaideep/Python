#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:26:26 2020

@author: nitinkotcherlakota
"""

def longestPeak(array):
    # Write your code here.
    i = 0
    j = i + 1
    k = i
    count = 0
    final = 0
    while j < len(array):
        if array[j] > array[k]:
            k += 1
            j += 1
            count += 1
        elif array[j] == array[k]:
            i = j
            k = i
            j = i + 1
            count = 0
        elif array[j] < array[k] and count > 0:
            final = j-i+1
            while array[j] < array[k]:
                k = j
                k += 1
            i = k
            k = i
            j = i + 1
            count = 0
    return final

print(longestPeak([1, 2, 3, 4, 5, 1]))
