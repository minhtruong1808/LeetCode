#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:08:07 2022

@author: truongminh
"""

arr = [1,1,2,3,4,5,'noo']

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool: #remember to define the type for the input parameter here, it is a list of array
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return 'True'
            hashset.add(i)
        
        return 'False'
    
sol = Solution()
print(sol.containsDuplicate(arr))