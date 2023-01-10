#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:27:25 2023

@author: truongmnguyen
"""

def frequencySort(string):
    hmap = {}
    freq = [[] for c in range(len(string) + 1)]
    for c in string:
        hmap[c] = 1 + hmap.get(c,0)
    for c,n in hmap.items():
        freq[n].append(c)
    
    out_str = []
    for i in range(len(freq)-1, 0, -1):
        if len(freq[i])!= 0:
            for e in sorted(freq[i]):
                out_str += e*i
    
    return out_str

print(frequencySort("cacacabu"))