#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:33:56 2020

@author: nitinkotcherlakota
"""

#Five star sellers
import heapq

def minimum_review(productRatings, threshold):

    heap = []
    times = 0

    for index, product in enumerate(productRatings):
        diff = get_diff(product)
        heapq.heappush(heap, (-diff, index))
    #print(heap)
    while cal_precentage(productRatings) < threshold:
        # 1. find out the one with largest diff
        largest_diff, idx = heapq.heappop(heap)
        largest_diff = -largest_diff  # not use at all
        
        # 2. add 1 on both numerator and denominator
        # update productRatings, also need to know which one has the largest diff
        productRatings[idx][0] += 1
        productRatings[idx][1] += 1

        # caclulate the new diff and push to heap
        new_product = [productRatings[idx][0], productRatings[idx][1]]
        #print(new_product)
        new_diff = get_diff(new_product)
        heapq.heappush(heap, (-new_diff, idx))

        times += 1

    return times


def get_diff(product):
    cur_rating = product[0] / product[1]
    changed_rating = (product[0] + 1) / (product[1] + 1)
    diff = changed_rating - cur_rating
    
    return diff

def cal_precentage(productRatings):
    cur_rating_sum = 0
    for product in productRatings:
        cur_rating_sum += product[0] / product[1]

    return cur_rating_sum*100 / len(productRatings)

input = [[4,4],[1,2],[3,6]]; th = 77
print(minimum_review(input, th))
