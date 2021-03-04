#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:00:13 2020

@author: nitinkotcherlakota
"""

def spiralTraverse(matrix):
    # Write your code here.
    rows = len(matrix)
    cols = len(matrix[0])
    step = 0
    start = 0
    end = 0
    final_array = []
    while start < rows and start >= 0 and end < cols and end >= 0:
        if len(matrix) * len(matrix[0]) == len(final_array):
            return final_array
        if step == 0:
            final_array.append(matrix[start][end])
            end += 1
            if end == cols:
                step += 1
                end = cols - 1
                start += 1
        elif step == 1:
            final_array.append(matrix[start][end])
            start += 1
            if start == cols:
                step += 1
                start = cols - 1
                end -= 1
        elif step == 2:
            final_array.append(matrix[start][end])
            end -= 1
            if end == 0:
                step += 1
                start = rows - 1
        elif step == 3:
            final_array.append(matrix[start][end])
            start -= 1
            if start == 1:
                step = 0
                rows -= 1
                cols -= 1
    return final_array

a = spiralTraverse([
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11],
        ])
print(a)