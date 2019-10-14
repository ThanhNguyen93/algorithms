#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:52:10 2019

@author: thanhng
"""

import math

def BUCKET_SORT(x):
    num_bucket= len(x)
  
    b = []
    for i in range(num_bucket): b.append([])

    for i in range(0, num_bucket):
        b_index = math.floor(num_bucket*x[i])
        #print(b_index)
       # print(b[b_index])
       # print(x[i])
        b[b_index].append(x[i])
       # print(b[b_index])
    
    for i in range(0, num_bucket):
        if len(b[i]) >1:
           # print(INSERTION_SORT_sua(b[i]))
            sorted_b = INSERTION_SORT(b[i])
            b[i] = sorted_b
            
    final = []
    for i in range(0, num_bucket):
        final.append(b[i])
       # print(final)
    return final

def INSERTION_SORT(lst):
    for j in range(1, len(lst)):
        key = lst[j]
       # print('j:', j)
       # print('key:', key)
        i = j-1
        #print('i:', i)
        #print('lst[i]:', lst[i])
        while i >=0 and lst[i]>key:
          #  print('lst[i]:', lst[i], 'key:', key)
            lst[i+1] = lst[i]
           # i = i-1
            i -=1
        lst[i+1] = key
       # print(lst, '\n')
    return lst
    
x = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434] 

x_1 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]


BUCKET_SORT(x)


        
