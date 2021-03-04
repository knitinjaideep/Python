#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 06:55:09 2020

@author: nitinkotcherlakota
"""

def reorderLogFiles(logs):
    return sorted(logs,key = sort)
def sort(logs):
        a,b = logs.split(' ', 1)
        if b[0].isalpha():
            return (0,b,a)
        else:
            return (1,None,None)
        
print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))