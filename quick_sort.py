# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:12:11 2018

@author: nidhi
#"""
#Reference:
#https://github.com/death667b/quickSort/blob/master/quick_sort.py
#"""Implement quick sort in Python.
#Input a list.
##Output a sorted list."""
#def quicksort(array):
#    pivot = array[0]
#    l = len(array)
#   for i in range l:
#       storeIndex = i + 1
#       for j in range(1, len(array)):
#           if array[j] < array[0]:
#               array[0] = array[j]
#               storeindex+=1
#               pivot = array[storeindex]
#           
#          if element[i] < element[pivot]
#
#      swap(i, storeIndex); storeIndex++
#
#  swap(pivot, storeIndex - 1)
#
#>
#slowfastgo to beginningprevious framepausenext framego to end
#
#    return array

#Quick Sort algo in Python3

""
import datetime
def quick_sort(arr):
    #quick_sort sorts an array of integers.
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
start = datetime.datetime.now()
print (quick_sort(test))
finish = datetime.datetime.now()
print ('time taken', finish-start)