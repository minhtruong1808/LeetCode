#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:41:52 2023

@author: truongmnguyen
"""

nums = [1,1,1,2,2,3]

def topKFrequent(nums, k):
    count = {}    # hash map with key as number and value as count
    freq = [[] for i in range(len(nums)+1)]  # array which hold list, 
    # the list contains the element with the count that corresponds to the index of the array   
    
    for i in nums:# generate the hash map
        count[i] = 1 + count.get(i,0)
    for i,c in count.items(): # add the element to the coresponding list in the array
        freq[c].append(i)
    
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res

print(topKFrequent(nums, 2))