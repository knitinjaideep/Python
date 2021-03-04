#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:15:49 2020

@author: nitinkotcherlakota
"""

#Fraudulent Activity



input1 = [['345366 89921 45'],['029323 38239 23'],['38239 345366 15'],['029323 38239 77'],['345366 38239 23'],['029323 345366 13'],['38239 38239 23']]
d = {}
frauds = []
for i in range(len(input1)):
    user1,user2 = input1[i][0].split()[0:2]
    
#    user1,user2,num = input1[i].split()
    if user1 not in d:
        d[user1] = 1
    else:
        d[user1] += 1
    if user2 not in d:
        d[user2] = 1
    else:
        d[user2] += 1
#print(sorted(d.items(),key = lambda x:x[1], reverse = True))
for user in d:
    if d[user] >= 3:
        frauds.append(user)
print(frauds)
#
#from collections import Counter
#def find_frauds(transactions, threshold):
#    frauds = []
#    if not transactions:
#        return frauds
#    user_counts = Counter()
#    #print(user_counts)
#    for transaction in transactions:
#        users = transaction[0].split()[0:2]
#        curr_users = Counter()
#        for user in users:
#            if user not in curr_users:
#                curr_users[user] += 1
#        for user in curr_users:
#            user_counts[user] += curr_users[user]
#    print(user_counts, curr_users)
#    for user in user_counts:
#        if user_counts[user] >= threshold:
#            frauds.append(user)
#    return frauds
#
#
#def main():
#    transactions1 = [
#        ["345366 89921 45"],
#        ["029323 38239 23"],
#        ["38239 345366 15"],
#        ["029323 38239 77"],
#        ["345366 38239 23"],
#        ["029323 345366 13"],
#        ["38239 38239 23"]
#    ]
#    print("The fradulent users are ", find_frauds(transactions1, 3))
#
#
#main()