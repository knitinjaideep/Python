#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:41:53 2020

@author: nitinkotcherlakota
"""

#Ceaser Cipher
def caesarCipherEncryptor(string, key):
    # Write your code here.
	len_o = len(string)
	last = string[len(string)-1]
	for i in range(key):
		new_key = CalNewKey(last)
		last = new_key
		string += new_key
	return string[len(string) - len_o:]
def CalNewKey(last):
	if ord(last) == 122:
		new_key = ord(last) - 25
		return chr(new_key)
	elif ord(last) >= 97:
		new_key = ord(last) + 1
		return chr(new_key)	

print(caesarCipherEncryptor('xyz',2))
