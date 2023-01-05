#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:26:18 2022

@author: truongminh
"""

def isPalindrome(x):
    x_list = [i for i in str(x)] # convert the string into a list - O(n) 
    
    rev_x_list = [] # empty list to hold the reverse string characters
    for i in range(len(x_list)-1,-1,-1): #transverse through the string backward - O(n)
        rev_x_list.append(x_list[i]) # add each value to the new list
        
    return x_list == rev_x_list