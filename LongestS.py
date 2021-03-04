#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:26:28 2020

@author: nitinkotcherlakota
"""

#Longest substring
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            if s[j] not in d or (s[j] in d and s[j] not in s[i:j+1]):
                d[s[j]] = j
                max_len = max(max_len, len(s[i:j+1]))
            elif s[j] in d:
                i = d[s[j]] + 1
                d[s[j]] = j
                
        return max_len
                
                
print(lengthOfLongestSubstring("tmmzuxt"))