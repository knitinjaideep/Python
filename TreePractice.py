#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:50:14 2020

@author: nitinkotcherlakota
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self,root):
        self.root = Node(root)
        
        