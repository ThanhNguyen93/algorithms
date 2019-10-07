#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:31:33 2019

@author: thanhng
"""

lst = [5,2,4,6,1,3]

lst = [1,2,4,5,3]

lst = [1,4, 3, 5, 6, 2]

lst = [8, 7, 6, 5, 4, 3, 2, 1]

#len(lst) = 6

for j in range(1, len(lst)):
    key = lst[j]
    print('j:', j)
    print('key:', key)
    i = j-1
    print('i:', i)
    print('lst[i]:', lst[i])
    while i>=0 and lst[i]>key:
        print('lst[i]:', lst[i], 'key:', key)
        lst[i+1] = lst[i]
        i = i-1
    lst[i+1] = key
    print(lst, '\n')
    
print(lst)



import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    
    key = arr[n]

    for i in range(key, -1, -1):
        print('arr[i]:', arr[i])
        print('key:', key)
        if arr[i]>key:
            arr[i+1] = arr[i]
            print(arr, '\n')
        else: 
            arr[i+1] = key
            print(arr, '\n')
     


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

input = '2 4 6 8 3'

int(input).
arr = [2,4,6,8,3]


size = int(input())

array = input().split(" ")
arr = ['None'] * size
for i in range(size):
    arr[i] = int(array[i])
i = 1   
while i < size:
    tmp = arr[i]
    j = i - 1
    while arr[j] > tmp and j > -1:
        arr[j+1] = arr[j]       
        j = j - 1 
    arr[j+1] = tmp
    for k in range(size):
        print(arr[k],end = " ")
    print()    
    i = i + 1

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
###########
n = int(input())
line = list(map(int, input().split()))



def  list_print(lst):
    print( ' '.join(map(str, lst) ) )

def insert(lst, i):
    """Insert element at ith position into sublist [0, i] inplace"""
    pos = i-1
    for pos in range(i-1, -1, -1):
        if lst[pos] > lst[pos+1]:
            lst[pos], lst[pos+1] = lst[pos+1], lst[pos]
                    
    
for stop in range(1, n):
    insert(line, stop)
    list_print(line)
    
    
num = input ("Enter number :") 
print(num)