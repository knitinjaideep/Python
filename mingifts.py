#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:18:26 2020

@author: nitinkotcherlakota
"""


def Gifts(number_of_employees, Rank):
    final = [1 for i in range(number_of_employees)]
    if (number_of_employees) == 2:
        if Rank[0] < Rank[1] or Rank[1] < Rank[0]:
            return sum(final) + 1
    for i in range(1,number_of_employees-1):
        if Rank[i-1] < Rank[i] and Rank[i+1] < Rank[i]:
            if final[i] <= final[i+1]:
                final[i] += 1
        elif Rank[i-1] < Rank[i] and Rank[i+1] > Rank[i]:
            if final[i+1] <= final[i] or final[i] <= final[i-1]:
                if final[i+1] == final[i] == final[i-1]:
                    final[i+1] += 2
                    final[i] += 1
                else:
                    final[i+1] += 1
                    final[i] += 1  
        elif Rank[i-1] > Rank[i] and Rank[i+1] < Rank[i]:
            if final[i-1] <= final[i] or final[i] <= final[i+1]:
                if final[i+1] == final[i] == final[i-1]:
                    final[i-1] += 2
                    final[i] += 1
                else:
                    final[i-1] += 1
                    final[i] += 1  
        elif Rank[i-1] > Rank[i] and Rank[i+1] > Rank[i]:
            if final[i-1] <= final[i]:
                final[i-1] += 1
            if final[i+1] <= final[i]:
                final[i+1] += 1
    return sum(final)


    
print (Gifts(5, [1,2,1,5,2]))