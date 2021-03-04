#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:09:44 2020

@author: nitinkotcherlakota
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i in range(len(nums)-1):
        match = target - nums[i]
        if match in d:
            return [i,d[target - nums[i]]]
        else:
            d[nums[i]] = i 
    return []

nums = [3,2,4]
target = 6
print(twoSum(nums,target))