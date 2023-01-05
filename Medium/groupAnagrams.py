#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:59:31 2023

@author: truongminh
"""

def groupAnagrams(strs):
    hmap = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        
        if sorted_s not in hmap.keys():
            hmap[sorted_s] = []
        
        hmap[sorted_s].append(s)
    
    return hmap.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))