#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:01:39 2020

@author: nitinkotcherlakota
"""

#Unique substrings with k distinct characters
def unique(s,k):
    result = []
    st = ''
    i = 0
    j = 0
    
    while j < len(s):
        if s[j] not in st and len(st) < k:
            st += s[j]
        elif s[j] in st and len(st) < k:
            i += 1
            j = i
            st = s[j]
        if len(st) >= k:
            if st not in result:
                result.append(st)
            st = st[i+1:j+1]
        j+=1
    return result

print(unique('abacab',3))
print(unique('abcabc',3))
print(unique(s = "awaglknagawunagwkwagl", k = 4))