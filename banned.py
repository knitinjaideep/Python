#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:03:28 2020

@author: nitinkotcherlakota
"""
import collections
def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """

    banset = set(banned)
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
        
    count = collections.Counter(
        word for word in paragraph.lower().split())

    ans, best = '', 0
    for word in count:
        if count[word] > best and word not in banset:
            ans, best = word, count[word]

    return ans

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))