#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:26:38 2022

@author: truongminh
"""

def twosum(nums, target):
    hashmap = {} # create a hashmap to store the values
    # the key will store the value in nums array while the value will store the index
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap.keys():
            return [hashmap[diff],i]
        hashmap[nums[i]] = i
    
    return None